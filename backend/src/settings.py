import os

BASEDIR = os.environ.get("BASEDIR") or os.path.dirname(__file__)
MAIN_SQL_DB_URL = os.environ["MAIN_SQL_DB_URL"]
