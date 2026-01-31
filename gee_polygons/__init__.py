__version__ = "0.0.4"

# Import modules that patch the Site class
from gee_polygons import extract  # noqa: F401 - adds extract_categorical, extract_continuous, show_layer

# Import collection classes for batch operations
from gee_polygons.collection import SiteCollection, ChunkedResult

# Import export classes
from gee_polygons.export import ExportDestination, ExportConfig, ExportTask

__all__ = [
    'SiteCollection',
    'ChunkedResult',
    'ExportDestination',
    'ExportConfig',
    'ExportTask',
]
