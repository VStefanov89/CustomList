from unittest import TestCase, main
from custom_list.lists import CustomList


class CustomListTest(TestCase):
    def test_append_method_and_return_list(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        my_list.append(4)
        self.assertEqual([1, 2, 3, 4], my_list._CustomList__elements)

    def test_remove_method_not_in_range_raises(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        with self.assertRaises(IndexError) as ex:
            removed_element = my_list.remove(-6)
        self.assertEqual("Index out of range", str(ex.exception))

    def test_remove_method_not_correct_value_raises(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        with self.assertRaises(ValueError) as ex:
            removed_element = my_list.remove("asd")
        self.assertEqual("Index is not a valid integer", str(ex.exception))


if __name__ == '__main__':
    main()
