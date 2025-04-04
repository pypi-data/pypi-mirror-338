import napari
from napari_plugin_engine import napari_hook_implementation
# Import the correct main widget class name
from .ropcop_segmenter_widget import RopCopSegmentationWidget

# Factory function to create and return the widget instance
def launch_ropcop_widget(viewer: 'napari.viewer.Viewer'):
    """Creates an instance of the RopCop Segmentation widget."""
    # You could add status/debug widgets here if needed, similar to landmarks example
    # For now, just instantiate the main widget
    widget = RopCopSegmentationWidget(viewer)
    return widget

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    """Provides the RopCop Segmentation widget factory to Napari."""
    # Return list of tuples: (factory_function, options_dict)
    # The 'name' will appear in the Plugins menu and as the default dock widget title.
    return [(launch_ropcop_widget, {"name": "mKw RopSeg"})]
