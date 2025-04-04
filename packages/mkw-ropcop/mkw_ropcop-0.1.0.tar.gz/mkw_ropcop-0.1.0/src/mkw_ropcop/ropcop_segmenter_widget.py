#!/usr/bin/env python3
# Standard library imports
import os
import sys
import shutil
import datetime
import traceback
import glob
import subprocess # Added for launching Napari
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

# Third-party imports
try:
    import polars as pl
    HAS_POLARS = True
except ImportError:
    HAS_POLARS = False
    print("ERROR: Polars library is required but not installed. Please install it (pip install polars).")

# QtPy imports
from qtpy.QtCore import Qt, Slot, QTimer, Signal
from qtpy.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QAbstractItemView,
    QLabel, QLineEdit, QFileDialog, QMessageBox, QProgressDialog, QApplication, QGroupBox,
    QPlainTextEdit, QListWidgetItem, QSizePolicy, QSlider, QToolButton, QSpacerItem,
    QInputDialog, QStyle, QSpinBox, QComboBox, QFormLayout, QCheckBox # Added QCheckBox
)
from qtpy.QtGui import QIcon, QPalette

# Numpy and Skimage
import numpy as np
from skimage.filters import sobel, threshold_otsu, rank, gaussian # Keep for edge magnitude calculation, add Otsu, add rank filters, add gaussian
from skimage.draw import polygon2mask # For creating mask from shapes layer
from skimage.morphology import disk, binary_dilation, binary_erosion # For local Z-score structuring element and hole filling
# from skimage.segmentation import active_contour # Removed for snake refinement
# from skimage.measure import find_contours # Removed for snake refinement
from skimage.util import img_as_ubyte, img_as_float # For converting image types

# Napari imports
try:
    import napari
    from napari.layers import Image as NapariImageLayer, Labels as NapariLabelsLayer, Shapes as NapariShapesLayer
    from napari.utils.notifications import show_info, show_error, show_warning
    # Import for saving layers utility (though we use layer.save directly)
    # from napari.layers.utils.layer_utils import save_layers
    HAS_NAPARI = True
except ImportError:
    show_info = print
    show_error = print
    show_warning = print
    NapariImageLayer = None
    NapariLabelsLayer = None
    NapariShapesLayer = None # Added
    HAS_NAPARI = False
    napari = None # type: ignore

# Constants
# ROUGH_LAYER_NAME = "Rough Ridge Segmentation" # Old name for Labels layer
ROUGH_SHAPES_LAYER_NAME = "Rough Polygon ROI" # New name for Shapes layer
REFINED_LAYER_NAME_SUFFIX = "_Refined_Ridge" # Suffix for the refined labels layer
PARQUET_DB_PATH = Path(os.path.expanduser("~")) / "coollab_dev" / "homebase_prime" / "dataframe" / "metal_database_base.parquet" # Centralized path

# --- RopCop Segmentation Widget ---
# This is the main widget you'll see docked in Napari.
class RopCopSegmentationWidget(QWidget):
    """
    Your friendly neighborhood ROP segmentation helper for Napari!

    This widget helps you:
      1. Select your main image.
      2. Draw a rough outline (ROI) around the ridge.
      3. Fine-tune the segmentation using thresholding and hole filling.
      4. Save your work.
    """
    def __init__(self, napari_viewer):
        super().__init__()
        if not HAS_NAPARI:
            self.setLayout(QVBoxLayout())
            self.layout().addWidget(QLabel("Napari not found. Please install napari."))
            return

        self.viewer = napari_viewer
        self.image_layer: Optional[NapariImageLayer] = None
        # self.rough_labels_layer: Optional[NapariLabelsLayer] = None # Replaced with Shapes layer
        self.rough_shapes_layer: Optional[NapariShapesLayer] = None # Layer for drawing your initial rough outline (polygon, path, points)
        self.refined_labels_layer: Optional[NapariLabelsLayer] = None # Layer where the final segmentation appears and gets edited
        self._rough_layer_event_connected = False # Internal flag to track if we're watching the shapes layer for changes

        # --- Status Bar and Debug Log ---
        # Shows messages about what's happening or if you need to do something.
        self.status_label = QLabel("Ready. Assign layers.")
        self.status_label.setMaximumHeight(25)

        self.debug_output = QPlainTextEdit()
        self.debug_output.setReadOnly(True)
        self.debug_output.setMaximumHeight(100) # Limit height

        # --- Layout ---
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5); main_layout.setSpacing(6)

        # --- Layer Assignment Group ---
        layer_group = QGroupBox("Layer Assignment")
        layer_layout = QVBoxLayout(layer_group)

        # --- Image Layer Selection ---
        image_select_layout = QHBoxLayout()
        image_select_layout.addWidget(QLabel("Enface Image:"))
        self.image_layer_combo = QComboBox()
        self.image_layer_combo.setToolTip("Pick the main 2D image you want to segment from the dropdown.")
        image_select_layout.addWidget(self.image_layer_combo, 1)
        layer_layout.addLayout(image_select_layout)

        # --- Assign Button ---
        self.assign_layers_button = QPushButton("Assign Layers / Refresh")
        self.assign_layers_button.setToolTip("Click this after selecting your image.\nIt finds or creates the needed 'Rough Polygon ROI' (Shapes) and 'Refined_Ridge' (Labels) layers.")
        self.assign_layers_button.clicked.connect(self._assign_layers)
        layer_layout.addWidget(self.assign_layers_button)

        # --- Assigned Layer Status Labels ---
        # These just confirm which layers the widget is currently working with.
        self.assigned_image_label = QLabel("Assigned Image: None")
        self.assigned_rough_shapes_label = QLabel("Assigned Rough ROI Shapes: None") # Shows the name of the shapes layer being used
        self.assigned_refined_label = QLabel("Assigned Refined Labels: None") # Shows the name of the labels layer being used
        for label in [self.assigned_image_label, self.assigned_rough_shapes_label, self.assigned_refined_label]:
            label.setStyleSheet("font-size: 8pt; color: gray;") # Make them small and gray
            layer_layout.addWidget(label)

        main_layout.addWidget(layer_group)

        # --- Segmentation Tools Group ---
        # This section holds all the buttons and sliders for actually doing the segmentation.
        # It's disabled until you assign layers.
        self.controls_group = QGroupBox("Segmentation Tools")
        self.controls_group.setEnabled(False) # Disabled until layers are assigned
        self._setup_segmentation_controls(self.controls_group) # Add all the buttons/sliders etc.
        main_layout.addWidget(self.controls_group)

        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)) # Spacer

        # --- Status Bar & Log Box ---
        log_group = QGroupBox("Log") # Renamed from Debug
        log_layout = QVBoxLayout(log_group)
        log_layout.setContentsMargins(2, 6, 2, 2); log_layout.setSpacing(2)
        log_layout.addWidget(self.debug_output) # The text box showing detailed messages

        main_layout.addWidget(self.status_label) # The one-line status message at the bottom
        main_layout.addWidget(log_group) # The log box

        self.setLayout(main_layout)

        # --- Connect Viewer Events & Initial Population ---
        self.viewer.layers.events.inserted.connect(self._refresh_image_layer_list)
        self.viewer.layers.events.removed.connect(self._refresh_image_layer_list)
        self.viewer.layers.events.reordered.connect(self._refresh_image_layer_list)
        self._refresh_image_layer_list() # Populate combo box initially

    # --- Layer Handling ---

    def _refresh_image_layer_list(self):
        """Updates the 'Enface Image' dropdown list with current 2D image layers."""
        current_selection = self.image_layer_combo.currentText() # Remember what was selected
        self.image_layer_combo.clear() # Clear the list
        found_current = False
        items = []
        for layer in self.viewer.layers:
            # Check if it's an Image layer and 2D
            if isinstance(layer, NapariImageLayer) and layer.ndim == 2:
                 items.append(layer.name)
                 if layer.name == current_selection:
                     found_current = True

        self.image_layer_combo.addItems([""] + sorted(items)) # Add blank option first

        if found_current:
            self.image_layer_combo.setCurrentText(current_selection)
        elif self.image_layer_combo.count() > 1: # If layers exist besides blank
             # Try to auto-select if only one suitable layer exists
             if len(items) == 1:
                 self.image_layer_combo.setCurrentText(items[0])
                 self._append_debug(f"Auto-selected image layer: {items[0]}")
                 # Optionally auto-assign here? Or wait for button press.
                 # QTimer.singleShot(0, self._assign_layers) # Auto-assign if desired
             else:
                 # Heuristic: prefer layers with 'enface' in the name?
                 enface_layers = [name for name in items if 'enface' in name.lower()]
                 if len(enface_layers) == 1:
                      self.image_layer_combo.setCurrentText(enface_layers[0])
                      self._append_debug(f"Auto-selected image layer: {enface_layers[0]}")
                      # QTimer.singleShot(0, self._assign_layers) # Auto-assign if desired

        self._append_debug("Updated the image layer dropdown.")

    @Slot()
    def _assign_layers(self):
        """Links the selected image to the widget and sets up the Shapes and Labels layers."""
        selected_image_name = self.image_layer_combo.currentText()

        # --- Disconnect old event handler if layer exists ---
        if self.rough_shapes_layer and self._rough_layer_event_connected:
            try:
                self.rough_shapes_layer.events.data.disconnect(self._on_shape_added)
                self._append_debug("Disconnected old shape event handler.")
            except (TypeError, RuntimeError): # Ignore errors if it wasn't connected
                pass
            self._rough_layer_event_connected = False

        # --- Reset everything ---
        self.image_layer = None
        self.rough_shapes_layer = None # Forget the old shapes layer
        self.refined_labels_layer = None # Forget the old labels layer
        self.controls_group.setEnabled(False) # Disable tools until layers are set
        # Clear the status labels
        self.assigned_image_label.setText("Assigned Image: None")
        self.assigned_rough_shapes_label.setText("Assigned Rough ROI Shapes: None")
        self.assigned_refined_label.setText("Assigned Refined Labels: None")
        self._set_status("Assigning layers...") # Update status bar

        if not selected_image_name:
            show_warning("Please select an enface image layer.")
            self._set_status("Select an image layer.")
            return

        try:
            img_layer = self.viewer.layers[selected_image_name]
            if not isinstance(img_layer, NapariImageLayer) or img_layer.ndim != 2:
                 show_error(f"Selected layer '{selected_image_name}' is not a 2D Image layer.")
                 self._set_status("Error: Select a valid 2D image.")
                 return
            self.image_layer = img_layer
            self._append_debug(f"Assigned Image Layer: {self.image_layer.name}")
            self.assigned_image_label.setText(f"Assigned Image: {self.image_layer.name}")

            # --- Find or Create the 'Rough Polygon ROI' Shapes Layer ---
            rough_shapes_name = ROUGH_SHAPES_LAYER_NAME # Get the standard name
            if rough_shapes_name in self.viewer.layers: # Check if a layer with this name exists
                layer = self.viewer.layers[rough_shapes_name]
                if isinstance(layer, NapariShapesLayer): # Is it the right type?
                    self.rough_shapes_layer = layer # Yes, use it!
                    # Maybe clear old shapes? For now, we keep them.
                    self._append_debug(f"Found existing Shapes Layer: {rough_shapes_name}")
                else: # Exists, but wrong type (e.g., an Image layer named the same)
                    self.viewer.layers.remove(layer) # Get rid of it
                    self._append_debug(f"Removed incorrect layer named '{rough_shapes_name}'. It wasn't a Shapes layer.")
                    self.rough_shapes_layer = None # Mark as not found
            # If it wasn't found, or we removed the wrong type, create a new one
            if self.rough_shapes_layer is None:
                self.rough_shapes_layer = self.viewer.add_shapes(
                    ndim=self.image_layer.ndim, # Make it 2D like the image
                    name=rough_shapes_name,
                    face_color='white', # Style it a bit
                    edge_color='blue',
                    opacity=0.3,
                    edge_width=2
                )
                self._append_debug(f"Created new Shapes Layer: {rough_shapes_name}")
            # Update the status label to show the name of the shapes layer we're using
            self.assigned_rough_shapes_label.setText(f"Assigned Rough ROI Shapes: {self.rough_shapes_layer.name}")

            # --- Watch the Shapes Layer for Changes ---
            # We want to automatically process a polygon right after it's drawn.
            if self.rough_shapes_layer and not self._rough_layer_event_connected:
                 # Connect the '_on_shape_added' function to the layer's data change event
                 self.rough_shapes_layer.events.data.connect(self._on_shape_added)
                 self._rough_layer_event_connected = True # Mark as connected
                 self._append_debug(f"Now watching '{self.rough_shapes_layer.name}' for new shapes.")


            # --- Find or Create the Refined Labels Layer ---
            # Name it based on the image layer + suffix (e.g., "MyImage_Refined_Ridge")
            refined_name = f"{self.image_layer.name}{REFINED_LAYER_NAME_SUFFIX}"
            if refined_name in self.viewer.layers: # Check if it exists
                layer = self.viewer.layers[refined_name]
                # Check if it's a Labels layer AND has the same size as the image
                if isinstance(layer, NapariLabelsLayer) and layer.shape == self.image_layer.shape:
                    self.refined_labels_layer = layer # Yes, use it!
                    self._append_debug(f"Found existing Labels Layer: {refined_name}")
                else: # Exists, but wrong type or size
                    self.viewer.layers.remove(layer) # Get rid of it
                    self._append_debug(f"Removed incorrect layer named '{refined_name}'. It wasn't a matching Labels layer.")
                    self.refined_labels_layer = None # Mark as not found
            # If it wasn't found or was removed, create a new one
            if self.refined_labels_layer is None:
                # Create an empty labels layer (all zeros) with the same shape as the image
                self.refined_labels_layer = self.viewer.add_labels(
                    np.zeros(self.image_layer.data.shape, dtype=np.int32),
                    name=refined_name
                )
                self._append_debug(f"Created new Labels Layer: {refined_name}")
            # Update the status label
            self.assigned_refined_label.setText(f"Assigned Refined Labels: {self.refined_labels_layer.name}")

            # --- Enable Tools and Finish Up ---
            self.controls_group.setEnabled(True) # Enable the segmentation buttons/sliders
            self._set_status("Layers assigned. Ready for segmentation.")
            # Make sure the brush size slider matches the layer's current brush size
            self._update_brush_size(self.size_slider.value())
            # Set the initial mode to 'Paint' on the refined layer
            self.mode_button.setChecked(False) # Ensure Paint/Erase button shows 'Paint'
            self._toggle_paint_mode(False) # Set the layer mode to 'paint'

        except KeyError:
            show_error(f"Layer '{selected_image_name}' not found in viewer.")
            self._set_status("Error: Layer not found.")
        except Exception as e:
            show_error(f"Error assigning layers: {e}")
            self._append_debug(traceback.format_exc())
            self._set_status("Error during layer assignment.")

    # --- Setting Up the Buttons and Sliders ---

    def _setup_segmentation_controls(self, parent_group):
        """Creates all the buttons, sliders, etc. for the 'Segmentation Tools' box."""
        layout = QVBoxLayout(parent_group)
        layout.setContentsMargins(5, 5, 5, 5) # Add some padding
        layout.setSpacing(5)

        # Use standard icons
        paint_icon = QIcon.fromTheme("tool-paintbrush", self.style().standardIcon(QStyle.SP_DialogResetButton))
        erase_icon = QIcon.fromTheme("tool-eraser", self.style().standardIcon(QStyle.SP_TrashIcon))
        polygon_icon = QIcon.fromTheme("draw-polygon", self.style().standardIcon(QStyle.SP_FileDialogDetailedView))
        path_icon = QIcon.fromTheme("draw-path", self.style().standardIcon(QStyle.SP_FileDialogListView)) # Placeholder
        points_icon = QIcon.fromTheme("draw-points", self.style().standardIcon(QStyle.SP_FileDialogInfoView)) # Placeholder
        save_icon = QIcon.fromTheme("document-save", self.style().standardIcon(QStyle.SP_DialogSaveButton))

        # --- Section 1: Drawing the Rough Outline ---
        rough_group = QGroupBox("1. Draw Rough Outline / Landmarks")
        rough_layout = QVBoxLayout(rough_group)

        # Buttons to activate Napari's drawing tools on the Shapes layer
        draw_buttons_layout = QHBoxLayout()

        # Polygon Button
        self.activate_polygon_button = QPushButton(polygon_icon, " Draw Polygon ROI")
        self.activate_polygon_button.setToolTip(f"Click this, then draw a polygon on the '{ROUGH_SHAPES_LAYER_NAME}' layer.\nThis defines the area where edge detection will happen.\nDouble-click or click the start point to finish.\n(Edge detection runs automatically when you finish!)")
        self.activate_polygon_button.clicked.connect(self._activate_shape_drawing)
        draw_buttons_layout.addWidget(self.activate_polygon_button)

        # Path Button (Optional, for landmarks maybe?)
        self.activate_path_button = QPushButton(path_icon, " Draw Path")
        self.activate_path_button.setToolTip(f"Activate path drawing tool on the '{ROUGH_SHAPES_LAYER_NAME}' layer (e.g., for tracing).")
        self.activate_path_button.clicked.connect(self._activate_path_drawing)
        draw_buttons_layout.addWidget(self.activate_path_button)

        # Points Button (Optional, for landmarks maybe?)
        self.activate_points_button = QPushButton(points_icon, " Place Points")
        self.activate_points_button.setToolTip(f"Activate points placement tool on the '{ROUGH_SHAPES_LAYER_NAME}' layer (e.g., for marking locations).")
        self.activate_points_button.clicked.connect(self._activate_points_drawing)
        draw_buttons_layout.addWidget(self.activate_points_button)

        rough_layout.addLayout(draw_buttons_layout)
        layout.addWidget(rough_group) # Add this section to the main layout

        # --- Section 2: Refining and Editing ---
        refine_group = QGroupBox("2. Refine & Edit Segmentation")
        refine_layout = QVBoxLayout(refine_group)

        # --- Manual Painting/Erasing ---
        paint_erase_group = QGroupBox("Manual Paint / Erase")
        paint_erase_layout = QVBoxLayout(paint_erase_group)

        # Brush Size Slider
        size_layout = QHBoxLayout()
        size_label = QLabel("Brush Size:")
        self.size_slider = QSlider(Qt.Horizontal)
        self.size_slider.setMinimum(1); self.size_slider.setMaximum(50); self.size_slider.setValue(10) # Range 1-50, default 10
        self.size_slider.setToolTip("Adjust the size of the paintbrush or eraser.")
        self.size_slider.setMinimumHeight(30)
        self.size_value_label = QLabel(str(self.size_slider.value())) # Shows the current size number
        self.size_value_label.setMinimumWidth(25)
        self.size_slider.valueChanged.connect(self._update_brush_size) # Link slider change to update function
        size_layout.addWidget(size_label); size_layout.addWidget(self.size_slider); size_layout.addWidget(self.size_value_label)
        paint_erase_layout.addLayout(size_layout)

        # Paint/Erase Toggle Button
        self.mode_button = QToolButton(); self.mode_button.setCheckable(True); self.mode_button.setText("Paint")
        self.mode_button.setToolTip("Switch between painting (adding to segmentation) and erasing (removing).")
        self.mode_button.setIcon(paint_icon)
        self.mode_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon); self.mode_button.setMinimumHeight(40)
        self.mode_button.toggled.connect(self._toggle_paint_mode) # Link toggle to update function
        paint_erase_layout.addWidget(self.mode_button)

        # Label ID (Value to paint with)
        label_id_layout = QHBoxLayout()
        label_id_layout.addWidget(QLabel("Label ID:"))
        self.label_id_spinbox = QSpinBox(); self.label_id_spinbox.setMinimum(1); self.label_id_spinbox.setMaximum(65535); self.label_id_spinbox.setValue(1)
        self.label_id_spinbox.setToolTip("Which label value to use when painting or running operations.\nUsually just keep this as 1 unless you need multiple distinct regions.")
        self.label_id_spinbox.setMinimumHeight(35)
        label_id_layout.addWidget(self.label_id_spinbox, 1)
        paint_erase_layout.addLayout(label_id_layout)

        refine_layout.addWidget(paint_erase_group) # Add paint/erase tools to the refine section

        # --- Automated Processing Tools ---
        processing_group = QGroupBox("Automated Processing")
        processing_layout = QVBoxLayout(processing_group); processing_layout.setSpacing(5)

        # --- Edge Detection Sub-Group ---
        edge_group = QGroupBox("Edge Detection (within Polygon ROI)")
        edge_layout = QVBoxLayout(edge_group)

        # Option: Detect Dark or Light Features
        self.detect_dark_checkbox = QCheckBox("Detect Dark Features (Invert Threshold)")
        self.detect_dark_checkbox.setToolTip("Check this box if the ridge is darker than its surroundings.\nLeave unchecked if the ridge is brighter.\nThis flips how the thresholds work.")
        # When checked/unchecked, re-run the edge detection using the current slider value
        self.detect_dark_checkbox.toggled.connect(lambda: self._on_edge_slider_changed(self.edge_thresh_slider.value()))
        edge_layout.addWidget(self.detect_dark_checkbox)

        # Edge Sensitivity Slider
        edge_thresh_layout = QHBoxLayout()
        edge_thresh_layout.addWidget(QLabel("Edge Sensitivity:")) # Renamed from Threshold
        self.edge_thresh_slider = QSlider(Qt.Horizontal)
        self.edge_thresh_slider.setMinimum(0); self.edge_thresh_slider.setMaximum(100); self.edge_thresh_slider.setValue(25) # 0-100 range, default 25
        self.edge_thresh_slider.setToolTip("Controls how sensitive the edge detection is.\nHigher values find stronger edges, lower values find fainter edges.\n(Applies Sobel edge detection after an initial Otsu brightness filter).")
        self.edge_thresh_value_label = QLabel(f"{self.edge_thresh_slider.value()/100.0:.2f}") # Display as 0.00 to 1.00
        self.edge_thresh_value_label.setMinimumWidth(35)
        # Update the label text when slider moves
        self.edge_thresh_slider.valueChanged.connect(lambda val: self.edge_thresh_value_label.setText(f"{val/100.0:.2f}"))
        # Update the actual segmentation preview when slider moves
        self.edge_thresh_slider.valueChanged.connect(self._on_edge_slider_changed)
        edge_thresh_layout.addWidget(self.edge_thresh_slider, 1)
        edge_thresh_layout.addWidget(self.edge_thresh_value_label)
        edge_layout.addLayout(edge_thresh_layout)

        # Manual Threshold Button (Now the only edge button)
        self.manual_edge_button = QPushButton("Apply Edge Threshold") # Renamed
        self.manual_edge_button.setToolTip("Find edges within the polygon ROI using the current 'Edge Sensitivity' setting.\n(Combines Otsu thresholding with Sobel edge detection).")
        self.manual_edge_button.setMinimumHeight(35)
        self.manual_edge_button.clicked.connect(self._run_manual_edge_detection)
        edge_layout.addWidget(self.manual_edge_button) # Add the button

        processing_layout.addWidget(edge_group) # Add edge detection tools to processing group

        # --- Hole Filling Sub-Group ---
        hole_fill_group = QGroupBox("Post-Processing")
        hole_fill_layout = QVBoxLayout(hole_fill_group)

        # Dilate/Contract Button
        self.dilate_contract_button = QPushButton("Fill Small Holes") # Renamed
        self.dilate_contract_button.setToolTip("Cleans up the segmentation by filling small gaps.\n(Performs morphological closing: dilation then erosion).")
        self.dilate_contract_button.setMinimumHeight(35)
        self.dilate_contract_button.clicked.connect(self._run_dilate_contract)
        hole_fill_layout.addWidget(self.dilate_contract_button)

        processing_layout.addWidget(hole_fill_group) # Add hole filling tools to processing group

        refine_layout.addWidget(processing_group) # Add processing group to the refine section

        # --- Section 3: Saving ---
        save_group = QGroupBox("3. Save Results")
        save_layout = QVBoxLayout(save_group)

        self.save_button = QPushButton(save_icon, " Save Segmentation & ROI")
        self.save_button.setToolTip("Saves the current 'Refined_Ridge' labels layer as a TIF file,\nthe 'Rough Polygon ROI' shapes layer as a CSV file,\nand updates the central Parquet database with the ROI info.")
        self.save_button.setMinimumHeight(40)
        self.save_button.clicked.connect(self._save_layers)
        save_layout.addWidget(self.save_button)

        refine_layout.addWidget(save_group) # Add save group to the refine section

        layout.addWidget(refine_group) # Add the whole "Refine & Edit" section to the main layout

    # --- Functions Called by Buttons/Sliders ---

    def _update_brush_size(self, value):
        """Sets the brush/eraser size on the Napari labels layer."""
        if self.refined_labels_layer:
            self.refined_labels_layer.brush_size = value # Tell Napari the new size
        self.size_value_label.setText(str(value)) # Update the text label next to the slider

    def _toggle_paint_mode(self, checked):
        """Switches the active tool on the labels layer between paint and erase."""
        paint_icon = QIcon.fromTheme("tool-paintbrush", self.style().standardIcon(QStyle.SP_DialogResetButton))
        erase_icon = QIcon.fromTheme("tool-eraser", self.style().standardIcon(QStyle.SP_TrashIcon))
        if self.refined_labels_layer:
            if checked: # 'checked' means the button is toggled ON (Erase mode)
                self.refined_labels_layer.mode = 'erase' # Tell Napari to erase
                self.mode_button.setText("Erase")
                self.mode_button.setIcon(erase_icon)
            else: # 'checked' is OFF (Paint mode)
                self.refined_labels_layer.mode = 'paint' # Tell Napari to paint
                self.mode_button.setText("Paint")
                self.mode_button.setIcon(paint_icon)
            # Make sure the labels layer is the active one in Napari so the tool works
            self.viewer.layers.selection.active = self.refined_labels_layer
        else: # If no labels layer is assigned, reset the button
            self.mode_button.setChecked(False)
            self.mode_button.setText("Paint")
            self.mode_button.setIcon(paint_icon)

    # --- Activating Napari's Drawing Tools ---

    @Slot()
    def _activate_shape_drawing(self):
        """Switches Napari to polygon drawing mode on the Shapes layer."""
        if not self.rough_shapes_layer:
            show_warning(f"Oops! The '{ROUGH_SHAPES_LAYER_NAME}' layer isn't set up. Click 'Assign Layers' first.")
            return
        # Make the shapes layer active and set the tool
        self.viewer.layers.selection.active = self.rough_shapes_layer
        self.rough_shapes_layer.mode = 'add_polygon'
        show_info(f"Ready to draw a polygon on '{self.rough_shapes_layer.name}'.\nDouble-click or click the start point to finish.\n(Edge detection runs automatically after!)")
        self._set_status("Drawing Rough Polygon ROI...")

    @Slot()
    def _activate_path_drawing(self):
        """Switches Napari to path drawing mode on the Shapes layer."""
        if not self.rough_shapes_layer:
            show_warning(f"Oops! The '{ROUGH_SHAPES_LAYER_NAME}' layer isn't set up. Click 'Assign Layers' first.")
            return
        self.viewer.layers.selection.active = self.rough_shapes_layer
        self.rough_shapes_layer.mode = 'add_path'
        show_info(f"Ready to draw a path on '{self.rough_shapes_layer.name}'.")
        self._set_status("Drawing Path...")

    @Slot()
    def _activate_points_drawing(self):
        """Switches Napari to points mode on the Shapes layer."""
        if not self.rough_shapes_layer:
            show_warning(f"Oops! The '{ROUGH_SHAPES_LAYER_NAME}' layer isn't set up. Click 'Assign Layers' first.")
            return
        self.viewer.layers.selection.active = self.rough_shapes_layer
        self.rough_shapes_layer.mode = 'add_points'
        show_info(f"Ready to place points on '{self.rough_shapes_layer.name}'.")
        self._set_status("Placing Points...")


    # --- Automatic Processing When Polygon is Drawn ---

    def _on_shape_added(self, event=None):
        """Runs automatically when you finish drawing a shape on the Shapes layer."""
        # This function gets called for *any* change to the shapes layer data.
        # We only care about when a *polygon* is finished.
        # A simple way is to check if the *last* shape added was a polygon.

        if not self.rough_shapes_layer or not self.image_layer:
            return # Safety check: Do nothing if layers aren't ready

        # Did we actually add a shape?
        if len(self.rough_shapes_layer.data) > 0:
            last_shape_type = self.rough_shapes_layer.shape_type[-1] # Check the type of the most recent shape
            if last_shape_type == 'polygon':
                self._append_debug(f"Polygon finished on '{self.rough_shapes_layer.name}'. Running initial edge detection...")
                # Get the sensitivity value from the slider
                initial_threshold = self.edge_thresh_slider.value() / 100.0
                # Run the edge detection (using Otsu mask for the first pass)
                # Use QTimer to run this *just after* the current event finishes, preventing potential issues.
                QTimer.singleShot(0, lambda: self._apply_edge_detection(threshold_value=initial_threshold, use_otsu_mask=True, use_zscore_auto=False))
            else:
                # If it wasn't a polygon (e.g., path or points), just log it and do nothing.
                self._append_debug(f"Ignoring non-polygon shape ({last_shape_type}) added/modified.")
        else:
             self._append_debug("Shapes layer is empty. Nothing to process.")


    # --- Edge Detection Functions ---

    @Slot(int)
    def _on_edge_slider_changed(self, value):
        """Runs automatically when you move the 'Edge Sensitivity' slider."""
        # This provides a live preview of the edge detection.
        threshold = value / 100.0
        # For the live preview, we skip the initial Otsu mask for speed.
        # Use QTimer to add a tiny delay (10ms) - helps prevent lag if you drag the slider quickly.
        QTimer.singleShot(10, lambda: self._apply_edge_detection(threshold_value=threshold, use_otsu_mask=False, use_zscore_auto=False))

    # --- This function is triggered by the "Apply Manual Threshold" button ---
    def _run_manual_edge_detection(self):
        """Applies edge detection using the current slider value, pre-masked by Otsu."""
        # This is the main way to apply the edge detection after drawing the polygon.
        threshold = self.edge_thresh_slider.value() / 100.0
        # Run the full detection including the Otsu pre-mask.
        self._apply_edge_detection(threshold_value=threshold, use_otsu_mask=True, use_zscore_auto=False) # use_zscore_auto is now always False

    # Removed _run_auto_edge_detection method

    # --- Hole Filling Function ---
    @Slot()
    def _run_dilate_contract(self):
        """Fills small holes in the segmentation using dilation then erosion."""
        if not self.refined_labels_layer:
            show_warning("Oops! The 'Refined_Ridge' layer isn't set up. Click 'Assign Layers' first.")
            return

        current_labels = np.asarray(self.refined_labels_layer.data) # Get the current segmentation data
        label_id = self.label_id_spinbox.value() # Get the ID we're working on

        # Make a temporary map of where the current label ID is
        binary_mask = (current_labels == label_id)
        if not np.any(binary_mask): # Check if there's anything to process
            show_warning(f"Hmm, couldn't find any pixels with label ID {label_id} to fill holes in.")
            self._set_status("No pixels to process.")
            return

        self._set_status("Filling holes...")
        self._append_debug(f"Starting hole filling for label ID {label_id}.")

        try:
            # How much to dilate/erode? A disk shape is usually good.
            # We could make this adjustable later.
            radius = 3
            selem = disk(radius) # Create a disk structuring element
            self._append_debug(f"Using a disk shape with radius {radius} for hole filling.")

            # Step 1: Dilate (expand) the labeled areas
            dilated_mask = binary_dilation(binary_mask, footprint=selem)
            self._append_debug("Dilation step done.")

            # Step 2: Erode (shrink) the dilated areas back down
            eroded_mask = binary_erosion(dilated_mask, footprint=selem)
            self._append_debug("Erosion step done.")
            # This dilation then erosion fills in small holes.

            # How many pixels did we add?
            filled_pixels = np.sum(eroded_mask) - np.sum(binary_mask)

            # Update the actual labels layer
            # We need to be careful not to erase other label IDs if they exist
            refined_update = current_labels.copy() # Make a copy to modify
            # Where the final mask is true, set the label ID
            refined_update[eroded_mask] = label_id

            # Put the updated data back into the layer
            self.refined_labels_layer.data = refined_update
            self.refined_labels_layer.refresh() # Tell Napari to redraw

            show_info(f"Filled holes using dilate/contract. Added about {filled_pixels} pixels.")
            self._set_status("Hole filling complete.")

        except Exception as e:
            show_error(f"Uh oh, something went wrong during hole filling: {e}")
            self._append_debug(traceback.format_exc())
            self._set_status("Error during hole filling.")


    # --- Saving Function ---
    @Slot()
    def _save_layers(self):
        """Saves the labels (TIF), shapes (CSV), and updates the database (Parquet)."""
        if not self.image_layer or not self.refined_labels_layer or not self.rough_shapes_layer:
            show_warning("Can't save yet. Make sure the Image, Refined Labels, and Rough ROI Shapes layers are assigned.")
            return
        if not HAS_POLARS: # Need the Polars library to handle the Parquet database
            show_error("Polars library not found. Cannot update the Parquet database.\nPlease install it (`pip install polars`).")
            return

        # --- Figure out where to save ---
        # Use the file path of the original image layer
        source_path = self.image_layer.source.path
        if not source_path:
            show_error("Can't figure out where to save. The assigned image layer doesn't seem to be linked to a file.")
            self._set_status("Save failed: Image has no file path.")
            return

        source_path = Path(source_path)
        save_dir = source_path.parent # Save in the same directory as the image
        base_name = source_path.stem # Get the image filename without extension (e.g., "scan123")
        scan_id = base_name # Use the filename stem as the unique ID for the database

        # --- Define filenames ---
        # Labels: e.g., "scan123_Refined_Ridge.tif"
        labels_filename = save_dir / f"{base_name}{REFINED_LAYER_NAME_SUFFIX}.tif"
        # Shapes: e.g., "scan123_roi_shapes.csv"
        shapes_filename = save_dir / f"{base_name}_roi_shapes.csv"
        # Database path (defined at the top of the file)
        parquet_path = PARQUET_DB_PATH

        self._set_status("Saving files and updating database...")
        self._append_debug(f"Saving Labels to: {labels_filename}")
        self._append_debug(f"Saving Shapes ROI to: {shapes_filename}")
        self._append_debug(f"Updating Database: {parquet_path} (Scan ID: {scan_id})")

        # --- Get Shapes Data Ready for Database ---
        # The database stores shape info (type and vertices) in a specific format.
        shapes_data_list = [] # Start with an empty list
        if self.rough_shapes_layer.data: # If there are any shapes on the layer...
            for i, vertices in enumerate(self.rough_shapes_layer.data):
                shape_type = self.rough_shapes_layer.shape_type[i] # Get 'polygon', 'path', etc.
                # Convert vertex coordinates (which might be numpy numbers) to standard Python floats
                # and store as a list of [y, x] pairs.
                vertices_list = [[float(coord[0]), float(coord[1])] for coord in vertices]
                # Add this shape's info to our list
                shapes_data_list.append({'type': shape_type, 'vertices': vertices_list})
        # Now shapes_data_list looks something like:
        # [{'type': 'polygon', 'vertices': [[y1,x1], [y2,x2], ...]}, {'type': 'point', 'vertices': [[y3,x3]]}]

        save_successful = True # Assume success initially

        try:
            # --- Save the TIF (Labels) and CSV (Shapes) files ---
            # Use Napari's built-in saving, which handles the file types automatically.
            self.refined_labels_layer.save(str(labels_filename), plugin='napari')
            self.rough_shapes_layer.save(str(shapes_filename), plugin='napari')
            self._append_debug(f"Saved {labels_filename.name} and {shapes_filename.name}")

            # --- Update the Parquet Database ---
            if not parquet_path.exists():
                 show_error(f"Database file not found at: {parquet_path}")
                 self._set_status("Save failed: Database file missing.")
                 return # Can't update if it's not there

            try:
                # Load the database
                df = pl.read_parquet(parquet_path)

                # Does it have the 'scan_id' column we need?
                if 'scan_id' not in df.columns:
                     show_error(f"The database file ({parquet_path}) is missing the required 'scan_id' column.")
                     self._set_status("Save failed: Database missing 'scan_id'.")
                     return

                # Find the row matching the current scan ID
                scan_exists = df.filter(pl.col('scan_id') == scan_id).height > 0

                if not scan_exists:
                    # If the scan ID isn't in the database, we can't update it.
                    # We could potentially add a new row here, but it's safer to just warn.
                    show_warning(f"Scan ID '{scan_id}' wasn't found in the database ({parquet_path}).\nShapes ROI data was NOT saved to the database.")
                    self._set_status("Warning: scan_id not found in Database.")
                    # We still saved the TIF/CSV, so don't mark as total failure yet.
                else:
                    # --- Update the existing row ---
                    target_col = 'ROI_Shapes_Data' # The column where we store the shapes list

                    # Define the expected data structure for Polars (List of Structs)
                    shapes_dtype = pl.List(pl.Struct([
                        pl.Field("type", pl.Utf8),
                        pl.Field("vertices", pl.List(pl.List(pl.Float64)))
                    ]))

                    # Make sure the column exists, if not, add it (filled with nulls)
                    if target_col not in df.columns:
                        df = df.with_columns(pl.lit(None, dtype=shapes_dtype).alias(target_col))
                    # If it exists but has the wrong type, log a warning. We'll overwrite it anyway.
                    elif df[target_col].dtype != shapes_dtype:
                         self._append_debug(f"Warning: Column '{target_col}' has wrong data type ({df[target_col].dtype}). Overwriting.")

                    # Update the specific row using Polars' `when/then/otherwise`
                    df = df.with_columns(
                        pl.when(pl.col('scan_id') == scan_id) # Find the row
                        .then(pl.lit(shapes_data_list, dtype=shapes_dtype)) # Put the new shapes data there
                        .otherwise(pl.col(target_col)) # Keep other rows as they were
                        .alias(target_col) # Name the resulting column
                    )

                    # Save the modified DataFrame back to the Parquet file
                    df.write_parquet(parquet_path)
                    self._append_debug(f"Updated database successfully for scan_id: {scan_id}")

            except Exception as pe: # Catch errors during database update
                 show_error(f"Error updating database file: {pe}")
                 self._append_debug(traceback.format_exc())
                 self._set_status("Error updating database.")
                 save_successful = False # Mark as failed

            # --- Final Status Message ---
            if save_successful:
                show_info(f"Saved:\n - Labels: {labels_filename.name}\n - ROI Shapes: {shapes_filename.name}\nTo folder: {save_dir}\nDatabase updated for scan_id: {scan_id}")
                self._set_status("Layers saved & database updated.")
            else:
                 # This happens if TIF/CSV saved but database failed
                 show_warning(f"Saved TIF/CSV files, but failed to update database for scan_id: {scan_id}")
                 self._set_status("Files saved, Database update failed.")


        except Exception as e: # Catch errors during TIF/CSV saving
            show_error(f"Error saving TIF/CSV files: {e}")
            self._append_debug(traceback.format_exc())
            self._set_status("Error saving files.")


    # --- Internal Helper Functions ---

    def _get_rough_mask(self) -> Optional[np.ndarray]:
        """Creates a boolean (True/False) map from the last drawn polygon."""
        # Returns a 2D array where True means inside the polygon.
        if not self.rough_shapes_layer or not self.image_layer:
            return None # Not ready
        if not self.rough_shapes_layer.data:
            # No shapes drawn yet, just return None quietly.
            return None

        # We only care about the *last* shape drawn, assuming it's the main ROI polygon.
        last_shape_index = len(self.rough_shapes_layer.data) - 1
        if self.rough_shapes_layer.shape_type[last_shape_index] != 'polygon':
             # If the last shape wasn't a polygon, we can't make a mask from it.
             return None

        polygon_vertices = self.rough_shapes_layer.data[last_shape_index] # Get the corner points
        image_shape = self.image_layer.data.shape[:2] # Get the Y, X dimensions of the image

        try:
            # Use skimage to draw the polygon onto a boolean array
            rough_mask = polygon2mask(image_shape, polygon_vertices)
            if not np.any(rough_mask): # Check if the mask is completely empty
                return None # Polygon might be outside the image bounds
            return rough_mask
        except Exception as e: # Catch errors during mask creation
            show_error(f"Error creating mask from polygon: {e}")
            self._append_debug(traceback.format_exc())
            self._set_status("Error creating mask.")
            return None


    def _apply_edge_detection(self, threshold_value=None, use_otsu_mask=True, use_zscore_auto=False):
        """The main workhorse for finding edges and updating the labels layer."""
        # `threshold_value`: The sensitivity from the slider (0.0 to 1.0).
        # `use_otsu_mask`: If True, first find bright/dark areas using Otsu, then apply Sobel threshold inside those areas.
        #                  If False (for live preview), just apply Sobel threshold inside the polygon.
        # `use_zscore_auto`: This is now always False, kept for consistency in calls.

        if not self.image_layer or not self.refined_labels_layer:
            return # Not ready

        # Get the mask for the area inside the drawn polygon
        rough_mask = self._get_rough_mask()
        if rough_mask is None:
            # If no polygon is drawn, we can't do edge detection.
            # Maybe clear the refined layer here? For now, just do nothing.
            # self.refined_labels_layer.data = np.zeros_like(self.refined_labels_layer.data)
            # self.refined_labels_layer.refresh()
            # self._set_status("Draw a polygon ROI first.")
            return

        label_id = self.label_id_spinbox.value() # Which label value to paint with
        image_data = np.asarray(self.image_layer.data) # Get the image pixel data
        # Start with a blank slate for the results
        refined_update = np.zeros_like(image_data, dtype=self.refined_labels_layer.data.dtype)

        final_edge_mask = None # This will hold the final True/False map of detected edges
        detect_dark = self.detect_dark_checkbox.isChecked() # Are we looking for dark or light features?

        try:
            # --- Manual Thresholding Logic ---
            if threshold_value is None: # Should not happen with auto-detect removed, but safety check
                self._append_debug("Error: Edge sensitivity threshold is missing.")
                return

            # Calculate edge strength using Sobel filter
            # Convert image to float (0.0 to 1.0 range) for Sobel
            image_data_float = img_as_float(image_data)
            sobel_mag = sobel(image_data_float) # Calculate edge magnitude

            # Normalize edge strength to be between 0 and 1
            min_val, max_val = sobel_mag.min(), sobel_mag.max()
            if max_val <= min_val: # Handle flat images (no edges)
                show_info("Image looks flat, no edges found.")
                self._set_status("No edges detected (flat image?).")
                return
            sobel_norm = (sobel_mag - min_val) / (max_val - min_val) # Normalized edge map

            # --- Apply Thresholds ---
            if use_otsu_mask:
                # This runs when clicking "Apply Edge Threshold" or after drawing polygon.
                # Step 1: Find generally bright/dark areas within the ROI using Otsu's method.
                status_prefix = f"Applying Threshold (Otsu + Sens={threshold_value:.2f})"
                self._set_status(f"{status_prefix}...")
                self._append_debug(f"Starting Otsu + Sobel edge detection (Detect Dark: {detect_dark}, Sensitivity={threshold_value:.2f}).")

                image_roi = image_data[rough_mask] # Get image pixels inside the polygon
                if image_roi.size == 0:
                    show_warning("The polygon ROI seems empty.")
                    self._set_status("Processing error (empty ROI).")
                    return

                # Calculate Otsu threshold on the ROI pixels
                # Handle case where ROI is constant brightness
                if np.ptp(image_roi) < 1e-6: # ptp = peak-to-peak (max-min)
                    otsu_thresh = image_roi.flat[0] # Use the constant value
                    self._append_debug("ROI is constant brightness. Using that value for Otsu threshold.")
                else:
                    otsu_thresh = threshold_otsu(image_roi) # Calculate the threshold
                self._append_debug(f"Otsu brightness threshold within ROI: {otsu_thresh:.2f}")

                # Create a mask based on Otsu threshold and the dark/light checkbox
                if detect_dark: # Find pixels darker than the Otsu threshold
                    otsu_mask = (image_data < otsu_thresh) & rough_mask
                else: # Find pixels brighter than the Otsu threshold
                    otsu_mask = (image_data > otsu_thresh) & rough_mask

                # Step 2: Apply the Sobel sensitivity threshold *only within the Otsu mask*.
                # We are always looking for *high* Sobel values (strong edges) here.
                final_edge_mask = (sobel_norm > threshold_value) & otsu_mask
                status_msg = f"Manual {'Dark' if detect_dark else 'Bright'} (Otsu+Sobel>{threshold_value:.2f})"

            else:
                # This runs during the live slider preview.
                # Just apply the Sobel sensitivity threshold directly within the polygon ROI.
                status_prefix = f"Previewing Threshold (Sens={threshold_value:.2f})"
                self._set_status(f"{status_prefix}...")
                # Apply Sobel threshold based on checkbox (detect dark means *low* Sobel value)
                if detect_dark:
                     final_edge_mask = (sobel_norm < threshold_value) & rough_mask # Find low edge strength for dark features? (Check this logic) - Maybe should still be > threshold? Let's assume > for now.
                     # Reverting to standard Sobel > threshold logic even for dark detect, Otsu handles the dark part.
                     final_edge_mask = (sobel_norm > threshold_value) & rough_mask
                     status_msg = f"Manual Dark Preview (Sobel>{threshold_value:.2f})" # Status reflects intent
                else:
                     final_edge_mask = (sobel_norm > threshold_value) & rough_mask # Find high edge strength
                     status_msg = f"Manual Bright Preview (Sobel>{threshold_value:.2f})"


            # --- Update the Labels Layer ---
            if final_edge_mask is not None:
                num_final_edge_pixels = np.sum(final_edge_mask) # Count how many edge pixels found
                self._append_debug(f"Found {num_final_edge_pixels} edge pixels using {status_msg}.")

                if num_final_edge_pixels > 0:
                    refined_update[final_edge_mask] = label_id # Set the edge pixels to the chosen label ID
                    self.refined_labels_layer.data = refined_update # Update the layer data
                    self.refined_labels_layer.refresh() # Tell Napari to redraw
                    self._set_status(f"{status_msg}: {num_final_edge_pixels} pixels found.")
                else:
                    # If no edges found, make sure the layer is cleared
                    self.refined_labels_layer.data = refined_update # refined_update is still all zeros
                    self.refined_labels_layer.refresh()
                    self._set_status(f"{status_msg}: No edge pixels found.")
            else:
                 # Should not happen now, but if mask calculation failed somehow, clear the layer
                 self.refined_labels_layer.data = refined_update
                 self.refined_labels_layer.refresh()
                 self._set_status("Edge detection failed to produce a mask.")


        except Exception as e:
            show_error(f"Error during edge detection: {e}")
            self._append_debug(traceback.format_exc())
            self._set_status("Error during edge detection.")


    # --- Removed the old _process_polygon_roi ---


    # --- Utility Functions ---

    def _append_debug(self, message):
        """Adds a message to the log box with a timestamp."""
        # This is just for showing more detailed info during development or debugging.
        if hasattr(self, 'debug_output') and self.debug_output:
            timestamp = datetime.datetime.now().strftime('%H:%M:%S')
            self.debug_output.appendPlainText(f"[{timestamp}] {message}")
            # Auto-scroll to the bottom
            scrollbar = self.debug_output.verticalScrollBar()
            if scrollbar: scrollbar.setValue(scrollbar.maximum())
        else: # Fallback if the widget isn't fully set up
            print(f"Log: [{datetime.datetime.now().strftime('%H:%M:%S')}] {message}")

    def _set_status(self, message):
        """Updates the single-line status bar at the bottom."""
        if hasattr(self, 'status_label') and self.status_label:
            self.status_label.setText(message)
        else: # Fallback
            print(f"Status: {message}")
