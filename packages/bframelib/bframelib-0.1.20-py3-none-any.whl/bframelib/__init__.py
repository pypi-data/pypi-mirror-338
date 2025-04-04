import os
import pathlib

PATH = os.path.dirname(__file__)
__version__ = "0.1.20"

# PATH must be exported first since subsequent modules reference it
from .client import Client, Source, DEFAULT_SOURCES
from .interpreter import Interpreter

SCHEMA_SQL = pathlib.Path(f'{PATH}/bootstrap_sql/0_init.sql').read_text()


