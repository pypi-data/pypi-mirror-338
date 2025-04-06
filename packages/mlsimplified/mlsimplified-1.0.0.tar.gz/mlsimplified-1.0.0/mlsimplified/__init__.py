try:
    from .model import Model
except ImportError as e:
    raise ImportError(
        "Failed to import MLSimplified. Make sure all dependencies are installed: "
        "pip install -r requirements.txt"
    ) from e

__version__ = "1.0.0"
__all__ = ["Model"] 