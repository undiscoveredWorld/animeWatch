import unittest
from models.core import crud
from models.schemes.anime import Anime
from models.schemes.auth import User


class MyTestCase(unittest.TestCase):
    def test_something(self):
        AnimeCrud = crud.crud_from_list([
            Anime(publisher=User(), original_name="1")
        ])


if __name__ == '__main__':
    unittest.main()
