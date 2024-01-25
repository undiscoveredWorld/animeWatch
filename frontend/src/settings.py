from os import environ, path

from utils import prepare_url

BASEDIR = environ.get("BASEDIR") or path.dirname(__file__)
BACKEND_URL = prepare_url(environ["BACKEND_URL"])
