import sys
import os
import subprocess
import traceback # Added for error logging
from pathlib import Path
from qtpy.QtCore import Qt, QSize, Slot
from qtpy.QtGui import QPixmap, QIcon
from qtpy.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QFileDialog, QListWidget, QListWidgetItem, QSplitter, QScrollArea, QComboBox, # Added QComboBox
    QMessageBox, QFrame, QTabWidget, QTableWidget, QTableWidgetItem,
    QAbstractItemView
)

# Import Polars
try:
    import polars as pl
    HAS_POLARS = True
except ImportError:
    pl = None
    HAS_POLARS = False
    print("WARNING: Polars library not found. Parquet loading will be disabled.")


# Import Napari and the widget
try:
    import napari
    from napari.utils.notifications import show_info, show_error
    from .ropcop_segmenter_widget import RopCopSegmentationWidget # Import the widget class
    HAS_NAPARI = True
except ImportError:
    napari = None
    RopCopSegmentationWidget = None
    show_info = print
    show_error = print
    HAS_NAPARI = False
    print("WARNING: Napari not found. Launch functionality will be disabled.")


class RopCopBrowserGUI(QWidget):
    """
    Standalone Qt GUI for browsing PNG images and launching Napari
    with selected images for the RopCop segmentation widget.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("mKw RopCop - Image Browser")
        self.setGeometry(100, 100, 800, 600) # x, y, width, height

        # Base path for structured data - initially unset
        self.base_data_directory = None

        self.selected_files = [] # Files selected in Local Browser list
        self.parquet_data = None # To store loaded parquet data

        # --- Main Layout ---
        main_layout = QVBoxLayout(self)

        # --- Tab Widget ---
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget) # Add tab widget to main layout

        # --- Tab 1: Local Browser ---
        local_browser_widget = QWidget()
        local_browser_layout = QVBoxLayout(local_browser_widget)
        local_browser_layout.setContentsMargins(0,0,0,0) # Remove margins for the tab content

        splitter = QSplitter(Qt.Horizontal)
        local_browser_layout.addWidget(splitter) # Add splitter to the tab's layout

        # --- Left Panel (within Splitter) ---
        left_panel = QFrame()
        left_layout = QVBoxLayout(left_panel)

        # --- Selection Controls ---
        # Base Directory Display and Browse
        base_dir_layout = QHBoxLayout()
        self.base_dir_label = QLabel("Base Dir: Not Selected") # Initial text
        self.base_dir_label.setToolTip("Select the base directory containing patient folders using 'Browse Base...' or 'Load Parquet'")
        browse_base_button = QPushButton("Browse Base...")
        browse_base_button.setToolTip("Select the base directory containing patient folders")
        browse_base_button.clicked.connect(self._browse_base_directory)
        base_dir_layout.addWidget(QLabel("Base Dir:"))
        base_dir_layout.addWidget(self.base_dir_label, 1)
        base_dir_layout.addWidget(browse_base_button)
        left_layout.addLayout(base_dir_layout)

        # Patient ID Selector
        patient_layout = QHBoxLayout()
        self.patient_combo = QComboBox()
        self.patient_combo.setToolTip("Select Patient ID (Requires Base Dir)")
        self.patient_combo.currentIndexChanged.connect(self._populate_sessions) # Connect signal
        self.patient_combo.setEnabled(False) # Initially disabled
        patient_layout.addWidget(QLabel("Patient:"))
        patient_layout.addWidget(self.patient_combo, 1)
        left_layout.addLayout(patient_layout)

        # Session Selector
        session_layout = QHBoxLayout()
        self.session_combo = QComboBox()
        self.session_combo.setToolTip("Select Session")
        self.session_combo.currentIndexChanged.connect(self._populate_eyes) # Connect signal
        session_layout.addWidget(QLabel("Session:"))
        session_layout.addWidget(self.session_combo, 1)
        left_layout.addLayout(session_layout)

        # Eye Selector
        eye_layout = QHBoxLayout()
        self.eye_combo = QComboBox()
        self.eye_combo.setToolTip("Select Eye (od/os)")
        self.eye_combo.currentIndexChanged.connect(self._populate_volume_pngs) # Connect signal
        eye_layout.addWidget(QLabel("Eye:"))
        eye_layout.addWidget(self.eye_combo, 1)
        left_layout.addLayout(eye_layout)

        # --- OR --- Simple File Finder Button ---
        find_images_button = QPushButton("Load Any PNG...") # Updated text
        find_images_button.setToolTip("Select individual PNG files directly")
        find_images_button.clicked.connect(self._find_images)
        left_layout.addWidget(find_images_button)

        # --- File List (Populated based on selections OR Find Images) ---
        file_list_label = QLabel("Selected PNG Files:") # Changed label slightly
        left_layout.addWidget(file_list_label)
        self.file_list_widget = QListWidget() # This remains the list of PNGs to load
        self.file_list_widget.setSelectionMode(QListWidget.ExtendedSelection) # Allow multiple selections
        self.file_list_widget.currentItemChanged.connect(self._preview_image)
        self.file_list_widget.itemSelectionChanged.connect(self._update_selected_files)
        left_layout.addWidget(self.file_list_widget)

        splitter.addWidget(left_panel)

        # --- Right Panel (within Splitter) ---
        right_panel = QFrame() # Keep using QFrame for visual separation if desired
        right_layout = QVBoxLayout(right_panel)
        # right_panel.setFrameShape(QFrame.StyledPanel) # Optional: Keep frame for style
        right_panel.setMaximumWidth(400) # Limit preview panel width

        # Preview Area
        self.preview_label = QLabel("Select a PNG file to preview")
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_label.setMinimumSize(200, 200)
        # Add scroll area for large images
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.preview_label)
        right_layout.addWidget(scroll_area, 1) # Allow preview to expand

        # Note: Launch button moved outside/below tabs

        splitter.addWidget(right_panel)
        splitter.setSizes([400, 400]) # Initial sizes for splitter panels

        # Add the local browser widget (containing the splitter) to the first tab
        self.tab_widget.addTab(local_browser_widget, "Local Browser")

        # --- Tab 2: NAS Import ---
        nas_import_widget = QWidget()
        nas_layout = QVBoxLayout(nas_import_widget)

        # Button to load parquet
        self.load_parquet_button = QPushButton("Load Scan Parquet File...")
        self.load_parquet_button.clicked.connect(self._load_parquet)
        if not HAS_POLARS:
            self.load_parquet_button.setEnabled(False)
            self.load_parquet_button.setToolTip("Polars library not installed (pip install polars)")
        nas_layout.addWidget(self.load_parquet_button)

        # Label to show loaded parquet path
        self.parquet_path_label = QLabel("No Parquet file loaded.")
        self.parquet_path_label.setWordWrap(True)
        nas_layout.addWidget(self.parquet_path_label)

        # Table to display scan info (adjust columns as needed)
        self.nas_scan_table = QTableWidget()
        self.nas_scan_table.setColumnCount(5) # Example: scan_id, id, session, eye, scan_time
        self.nas_scan_table.setHorizontalHeaderLabels(["Scan ID", "Patient ID", "Session", "Eye", "Scan Time"])
        self.nas_scan_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.nas_scan_table.setEditTriggers(QAbstractItemView.NoEditTriggers) # Read-only
        self.nas_scan_table.verticalHeader().setVisible(False) # Hide row numbers
        self.nas_scan_table.horizontalHeader().setStretchLastSection(True)
        # Connect selection change if needed later for loading specific scans
        # self.nas_scan_table.itemSelectionChanged.connect(self._on_nas_scan_selected)
        nas_layout.addWidget(self.nas_scan_table)

        self.tab_widget.addTab(nas_import_widget, "NAS Import")


        # --- Launch Button (Below Tabs) ---
        launch_button = QPushButton("Launch Napari with Selected Images")
        launch_button.setStyleSheet("background-color: #28a745; color: white; font-weight: bold;")
        launch_button.clicked.connect(self._launch_napari)
        main_layout.addWidget(launch_button) # Add launch button below the tab widget

        # --- Initial Population ---
        self._populate_patient_ids() # Start population chain


    # --- Population Methods for Local Browser ---

    def _populate_patient_ids(self):
        """Populates the Patient ID combo box based on subdirectories."""
        self.patient_combo.clear()
        self.session_combo.clear()
        self.eye_combo.clear()
        self.file_list_widget.clear()
        self.patient_combo.addItem("") # Add empty initial item
        self.patient_combo.setEnabled(False) # Keep disabled until populated

        if self.base_data_directory and self.base_data_directory.is_dir():
            try:
                patient_dirs = sorted([d.name for d in self.base_data_directory.iterdir() if d.is_dir() and d.name.isdigit()])
                if patient_dirs:
                    self.patient_combo.addItems(patient_dirs)
                    self.patient_combo.setEnabled(True) # Enable if patients found
                    print(f"Found patient IDs: {patient_dirs}")
                else:
                    print(f"No patient ID subdirectories found in {self.base_data_directory}")
                    self.patient_combo.setEnabled(False)
            except Exception as e:
                QMessageBox.warning(self, "Scan Error", f"Error scanning for patient IDs in {self.base_data_directory}:\n{e}")
                self.patient_combo.setEnabled(False)
        else:
            print(f"Base directory is not set or not valid: {self.base_data_directory}")
            self.patient_combo.setEnabled(False)

    def _populate_sessions(self):
        """Populates the Session combo box based on selected Patient ID."""
        self.session_combo.clear()
        self.eye_combo.clear()
        self.file_list_widget.clear()
        self.session_combo.addItem("")

        patient_id = self.patient_combo.currentText()
        if patient_id and self.base_data_directory:
            patient_path = self.base_data_directory / patient_id
            if patient_path.is_dir():
                try:
                    session_dirs = sorted([d.name for d in patient_path.iterdir() if d.is_dir() and d.name.isdigit()])
                    self.session_combo.addItems(session_dirs)
                    print(f"Found sessions for patient {patient_id}: {session_dirs}")
                except Exception as e:
                    QMessageBox.warning(self, "Scan Error", f"Error scanning for sessions in {patient_path}:\n{e}")

    def _populate_eyes(self):
        """Populates the Eye combo box based on selected Patient and Session."""
        self.eye_combo.clear()
        self.file_list_widget.clear()
        self.eye_combo.addItem("")

        patient_id = self.patient_combo.currentText()
        session = self.session_combo.currentText()
        if patient_id and session and self.base_data_directory:
            session_path = self.base_data_directory / patient_id / session
            if session_path.is_dir():
                try:
                    # Look for 'od' or 'os' directories
                    eye_dirs = sorted([d.name for d in session_path.iterdir() if d.is_dir() and d.name in ['od', 'os']])
                    self.eye_combo.addItems(eye_dirs)
                    print(f"Found eyes for patient {patient_id}, session {session}: {eye_dirs}")
                except Exception as e:
                    QMessageBox.warning(self, "Scan Error", f"Error scanning for eyes in {session_path}:\n{e}")

    def _populate_volume_pngs(self):
        """Populates the file list with PNGs from the 'volume' subdirectories."""
        self.file_list_widget.clear()
        self.selected_files = [] # Clear selection when repopulating

        patient_id = self.patient_combo.currentText()
        session = self.session_combo.currentText()
        eye = self.eye_combo.currentText()

        if patient_id and session and eye and self.base_data_directory:
            eye_path = self.base_data_directory / patient_id / session / eye
            if eye_path.is_dir():
                print(f"Scanning for scan times under: {eye_path}")
                found_pngs = []
                try:
                    # Iterate through potential scan_time directories
                    for scan_time_dir in eye_path.iterdir():
                        if scan_time_dir.is_dir(): # Check if it's a directory (could be files too)
                            volume_dir = scan_time_dir / "volume" # Changed from enface_images
                            if volume_dir.is_dir():
                                print(f"  Checking volume dir: {volume_dir}")
                                pngs_in_volume = sorted(volume_dir.glob('*.png'))
                                for png_file in pngs_in_volume:
                                    item = QListWidgetItem(f"{scan_time_dir.name}/volume/{png_file.name}") # Display relative path
                                    item.setData(Qt.UserRole, png_file) # Store full path
                                    item.setToolTip(str(png_file)) # Show full path on hover
                                    self.file_list_widget.addItem(item)
                                    found_pngs.append(png_file)
                    print(f"Found {len(found_pngs)} PNG files.")
                except Exception as e:
                    QMessageBox.warning(self, "Scan Error", f"Error scanning for PNGs in {eye_path}:\n{e}")
            else:
                 print(f"Eye path does not exist or is not a directory: {eye_path}")
        else:
            # Clear list if any selection is missing
            print("Selections incomplete, clearing file list.")


    # --- NAS Import Methods ---

    @Slot()
    def _load_parquet(self):
        """Opens a dialog to select a Parquet file and loads scan data."""
        if not HAS_POLARS:
            QMessageBox.critical(self, "Error", "Polars library is required but not installed.\nPlease install 'polars'.")
            return

        # Use current base directory if set, otherwise home
        start_dir = str(self.base_data_directory) if self.base_data_directory else str(Path.home())
        file_path_tuple = QFileDialog.getOpenFileName(
            self,
            "Load Scan Parquet File",
            start_dir,
            "Parquet Files (*.parquet);;All Files (*)"
        )
        parquet_path_str = file_path_tuple[0]

        if parquet_path_str:
            parquet_path = Path(parquet_path_str)
            try:
                print(f"Loading Parquet file: {parquet_path}")
                self.parquet_data = pl.read_parquet(parquet_path)
                print(f"Loaded DataFrame shape: {self.parquet_data.shape}")
                # Optional: Print first few rows for debugging
                # print("Parquet Head:\n", self.parquet_data.head())

                self.parquet_path_label.setText(f"Loaded: {self._shorten_path(parquet_path, max_len=70)}")
                self.parquet_path_label.setToolTip(str(parquet_path))

                # Populate the table
                self._populate_nas_table()

                # Update the base data directory for the local browser
                new_base_dir = parquet_path.parent
                if new_base_dir.is_dir():
                    self.base_data_directory = new_base_dir
                    self.base_dir_label.setText(f"Base Dir: {self._shorten_path(self.base_data_directory)}")
                    self.base_dir_label.setToolTip(str(self.base_data_directory))
                    self._populate_patient_ids() # Trigger refresh of local browser selectors
                    self.tab_widget.setCurrentIndex(0) # Switch back to local browser tab
                    print(f"Set local browser base directory to: {self.base_data_directory}")
                else:
                    # Use new_base_dir variable consistent with the message
                    QMessageBox.warning(self, "Warning", f"Could not access directory of Parquet file:\n{new_base_dir}")

            except Exception as e:
                error_msg = f"Failed to load or process Parquet file:\n{parquet_path}\n\nError: {e}"
                print(f"ERROR: {error_msg}")
                print(traceback.format_exc())
                QMessageBox.critical(self, "Parquet Load Error", error_msg)
                self.parquet_data = None
                self.parquet_path_label.setText("Error loading Parquet file.")
                self.nas_scan_table.setRowCount(0) # Clear table on error

    def _populate_nas_table(self):
        """Populates the QTableWidget with data from the loaded Parquet file."""
        if self.parquet_data is None:
            self.nas_scan_table.setRowCount(0)
            return

        # --- Define expected columns (adjust as needed based on actual parquet structure) ---
        # You mentioned: scan_id, id, session, eye, scan_time, and file locations (xml, png, proc)
        display_cols = ['scan_id', 'id', 'session', 'eye', 'scan_time']
        # Check if columns exist
        missing_cols = [col for col in display_cols if col not in self.parquet_data.columns]
        if missing_cols:
             QMessageBox.warning(self, "Parquet Format Warning",
                                 f"The loaded Parquet file is missing expected columns for display: {', '.join(missing_cols)}")
             # Adjust display_cols to only include available ones
             display_cols = [col for col in display_cols if col in self.parquet_data.columns]
             if not display_cols:
                 self.nas_scan_table.setRowCount(0)
                 return # Cannot display anything

        # Update table headers if needed (e.g., if columns were missing)
        self.nas_scan_table.setColumnCount(len(display_cols))
        self.nas_scan_table.setHorizontalHeaderLabels([col.replace('_', ' ').title() for col in display_cols])

        # Select and potentially convert data for display
        try:
            display_df = self.parquet_data.select(display_cols)
            num_rows = display_df.height
            self.nas_scan_table.setRowCount(num_rows)

            for row_idx in range(num_rows):
                for col_idx, col_name in enumerate(display_cols):
                    item_data = display_df[row_idx, col_idx]
                    # Convert Polars data types to string for QTableWidgetItem
                    item_text = str(item_data)
                    table_item = QTableWidgetItem(item_text)
                    # Optional: Add tooltip with full data if needed
                    # table_item.setToolTip(item_text)
                    self.nas_scan_table.setItem(row_idx, col_idx, table_item)

            self.nas_scan_table.resizeColumnsToContents() # Adjust column widths
            print(f"Populated NAS table with {num_rows} rows.")

        except Exception as e:
            error_msg = f"Error populating table from Parquet data:\n{e}"
            print(f"ERROR: {error_msg}")
            print(traceback.format_exc())
            QMessageBox.critical(self, "Table Population Error", error_msg)
            self.nas_scan_table.setRowCount(0)


    # --- Local Browser Methods ---

    @Slot()
    def _browse_base_directory(self):
        """Opens a dialog to select a new base directory for the structured browser."""
        # Start browsing from home or the last valid base directory
        start_dir = str(self.base_data_directory) if self.base_data_directory else str(Path.home())
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "Select Base Data Directory (containing Patient ID folders)",
            start_dir,
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        if dir_path:
            new_base_dir = Path(dir_path)
            if new_base_dir.is_dir():
                self.base_data_directory = new_base_dir
                self.base_dir_label.setText(f"Base Dir: {self._shorten_path(self.base_data_directory)}")
                self.base_dir_label.setToolTip(str(self.base_data_directory))
                self._populate_patient_ids() # Repopulate based on new base directory
            else:
                 QMessageBox.warning(self, "Invalid Directory", f"Selected path is not a valid directory:\n{new_base_dir}")

    @Slot()
    def _find_images(self):
        """Opens a dialog to select multiple PNG files directly."""
        # Start browsing from the base directory if set, otherwise home
        start_dir = str(self.base_data_directory) if self.base_data_directory else str(Path.home())
        file_paths_tuple = QFileDialog.getOpenFileNames(
            self,
            "Select PNG Image Files",
            start_dir,
            "PNG Files (*.png);;All Files (*)"
        )
        selected_paths_str = file_paths_tuple[0]

        if selected_paths_str:
            # Clear structured selections
            self.patient_combo.setCurrentIndex(0) # Reset patient dropdown
            # Session and Eye will clear automatically due to signal chain

            # Clear and populate the file list
            self.file_list_widget.clear()
            temp_selected_files = []
            for file_str in selected_paths_str:
                png_path = Path(file_str)
                if png_path.is_file() and png_path.suffix.lower() == '.png':
                    item = QListWidgetItem(png_path.name) # Display just the filename
                    item.setData(Qt.UserRole, png_path) # Store full path
                    item.setToolTip(str(png_path)) # Show full path on hover
                    self.file_list_widget.addItem(item)
                    temp_selected_files.append(png_path)
                else:
                    print(f"Skipping non-PNG or non-file: {png_path}")

            # Update the main selection list used by launch button
            self.selected_files = temp_selected_files
            print(f"Selected {len(self.selected_files)} files directly.")
            # Manually trigger selection update signal if needed, though setting items should do it
            # self._update_selected_files() # Call this just in case itemSelectionChanged doesn't fire


    def _shorten_path(self, path: Path, max_len=50) -> str:
        """Shortens a path string for display."""
        path_str = str(path)
        if len(path_str) > max_len:
            return "..." + path_str[-(max_len-3):]
        return path_str

    # Keep _preview_image and _update_selected_files as they work on file_list_widget

    @Slot(QListWidgetItem, QListWidgetItem)
    def _preview_image(self, current: QListWidgetItem, previous: QListWidgetItem):
        """Displays a preview of the currently selected PNG image."""
        if current:
            file_path: Path = current.data(Qt.UserRole)
            try:
                pixmap = QPixmap(str(file_path))
                if pixmap.isNull():
                     # Use file_path.name which is just the filename
                     self.preview_label.setText(f"Cannot load preview for\n{file_path.name}")
                else:
                    # Scale pixmap to fit the label while maintaining aspect ratio
                    scaled_pixmap = pixmap.scaled(self.preview_label.size() * 0.95, # Scale slightly smaller than label
                                                  Qt.KeepAspectRatio,
                                                  Qt.SmoothTransformation)
                    self.preview_label.setPixmap(scaled_pixmap)
            except Exception as e:
                self.preview_label.setText(f"Error loading preview:\n{e}")
        else:
            self.preview_label.setText("Select a PNG file to preview")

    @Slot()
    def _update_selected_files(self):
        """Updates the list of selected file paths from the file_list_widget."""
        self.selected_files = [item.data(Qt.UserRole) for item in self.file_list_widget.selectedItems()]
        # print(f"Selected files: {[str(f) for f in self.selected_files]}") # Debug print

    @Slot()
    def _launch_napari(self):
        """Launches Napari, loads selected images, and adds the RopCop widget."""
        if not HAS_NAPARI:
            QMessageBox.critical(self, "Error", "Napari is not installed or could not be imported.\nPlease install napari (`pip install napari[all]`) to use this feature.")
            return

        if not self.selected_files:
            QMessageBox.warning(self, "No Files Selected", "Please select one or more PNG images from the list.")
            return

        try:
            # 1. Get or create a Napari viewer
            try:
                viewer = napari.current_viewer()
                if viewer:
                    print("Using existing Napari viewer.")
                else:
                    print("Creating new Napari viewer.")
                    viewer = napari.Viewer()
            except Exception:
                print("Creating new Napari viewer (current_viewer failed).")
                viewer = napari.Viewer() # Fallback to create a new one

            # 2. Load selected images
            print(f"Loading {len(self.selected_files)} image(s) into Napari...")
            loaded_layers = []
            for file_path in self.selected_files:
                try:
                    # Ensure file_path is a Path object before converting to str
                    if isinstance(file_path, Path):
                        layers = viewer.open(str(file_path), plugin='builtins') # Specify plugin if needed
                        if layers:
                            loaded_layers.extend(layers)
                            print(f" - Loaded: {file_path.name}")
                        else:
                             print(f" - Warning: No layers returned for {file_path.name}")
                    else:
                        print(f" - Warning: Skipping invalid file path type: {type(file_path)}")
                except Exception as e:
                    error_msg = f"Failed to load image: {file_path}\nError: {e}"
                    print(error_msg)
                    QMessageBox.warning(self, "Load Error", error_msg)
                    # Optionally continue loading other images or stop

            if not loaded_layers:
                 QMessageBox.warning(self, "Load Error", "Could not load any of the selected images into Napari.")
                 return

            # 3. Instantiate and add the RopCop widget
            # Check if the widget is already present
            widget_name = "mKw RopSeg" # Must match the name in _dock_widget.py
            existing_widgets = viewer.window._dock_widgets
            if widget_name not in existing_widgets:
                print(f"Adding '{widget_name}' dock widget...")
                # Instantiate the widget, passing the viewer
                ropcop_widget_instance = RopCopSegmentationWidget(viewer)
                # Add the instance as a dock widget
                viewer.window.add_dock_widget(ropcop_widget_instance, name=widget_name, area='right')
                print(f"'{widget_name}' added successfully.")
            else:
                print(f"'{widget_name}' dock widget already exists.")
                # Optionally bring the existing widget to front if needed/possible

            # Optional: Bring the Napari window to the front (might not be necessary)
            # viewer.window._qt_window.raise_()
            # viewer.window._qt_window.activateWindow()

            # Optional: Close the browser GUI after launching Napari
            # self.close()

        except Exception as e:
            error_msg = f"An error occurred while launching Napari or adding the widget:\n{e}"
            print(f"ERROR: {error_msg}")
            print(traceback.format_exc())
            QMessageBox.critical(self, "Napari Launch Error", error_msg)
