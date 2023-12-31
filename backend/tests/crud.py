import unittest
from models.core.schemes import Model
from models.core import crud
from models.schemes.anime import Studio


class CRUDFromListTest(unittest.TestCase):
    def test_create_crud(self):
        # Create by crud_from_list
        elements: list[Model] = [
            Studio(id=0, name="Alchemy", description="Alchemy"),
            Studio(id=1, name="KWorks", description=""),
        ]

        studioCrud = crud.crud_from_list(elements)
        studioCrud.elements = elements
        studioCrud2 = crud.crud_from_list([])

        assert studioCrud is not studioCrud2
        self.assertNotEqual(studioCrud.elements, studioCrud2.elements)


    def test_read_all(self):
        # Standard case
        elements: list[Model] = [
            Studio(id=0, name="Alchemy", description="Alchemy"),
            Studio(id=1, name="KWorks", description=""),
        ]

        studioCrud = crud.CRUDFromList
        studioCrud.elements = elements
        all = studioCrud.read_all()

        self.assertEqual(all, elements)

        # elements is empty
        elements: list[Model] = []

        studioCrud = crud.CRUDFromList
        studioCrud.elements = elements
        all = studioCrud.read_all()

        self.assertEqual(all, elements)

        # elements stores non-model
        class A:
            pass

        with self.assertRaises(Exception) as context:
            elements: list[Model] = [A()]

            studioCrud = crud.CRUDFromList
            studioCrud.elements = elements
            all = studioCrud.read_all()

    def test_read(self):
        elements: list[Model] = [
            Studio(id=0, name="Alchemy", description="Alchemy"),
            Studio(id=1, name="KWorks", description=""),
        ]
        studioCrud = crud.CRUDFromList
        studioCrud.elements = elements
        instance = studioCrud.read(1, )

        self.assertEqual(instance, elements[1])

if __name__ == '__main__':
    unittest.main()
