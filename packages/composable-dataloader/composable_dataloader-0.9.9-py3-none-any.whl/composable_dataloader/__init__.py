"""
Framework for building data loaders with Ibis queries.

Supports running data loaders via CLI with DuckDB/Spark Connect 
or as Databricks Asset Bundle (DAB) workflows.
"""

__version__ = "0.1.0"

# Core components
from composable_dataloader.base_data_loader import DataLoader, Mode
from composable_dataloader.engine import QueryEngine, get_connection
from composable_dataloader.format import Format
from composable_dataloader.logger import logger

# Specialized loaders
from composable_dataloader.databricks import DatabricksDataLoader

# Make commonly used Typer components available
from typer import Option
from typing_extensions import Annotated

# Convenience exports
__all__ = [
    # Core components
    "DataLoader",
    "DatabricksDataLoader",
    "QueryEngine",
    "Format",
    "Mode",
    "logger",
    # Utilities
    "get_connection",
    # Type annotations
    "Annotated",
    "Option",
]
