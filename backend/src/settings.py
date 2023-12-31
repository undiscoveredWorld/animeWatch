"""
Stores all settings of the application

list of settings:
    BASEDIR - the base directory of the application
"""

import os

BASEDIR = os.environ.get("BASEDIR") or os.path.dirname(__file__)
