"""
Mosaia SDK initialization
"""
from .mosaia import Mosaia

__version__ = "0.1.0"

# Define what gets exported with "from mosaia import *"
__all__ = ['Mosaia']