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
            my_list.remove(-6)
        self.assertEqual("Index out of range", str(ex.exception))

    def test_remove_method_not_correct_value_raises(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        with self.assertRaises(ValueError) as ex:
            my_list.remove("asd")
        self.assertEqual("Index is not a valid integer", str(ex.exception))

    def test_remove_method(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        removed_element = my_list.remove(1)
        self.assertEqual(2, removed_element)

    def test_get_method_raises(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        with self.assertRaises(IndexError) as ex:
            my_list.get(6)
        self.assertEqual("Index out of range", str(ex.exception))

    def test_get_method(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)
        value =  my_list.get(0)
        self.assertEqual(1, value)

    def test_extend_method_raises(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        with self.assertRaises(ValueError) as ex:
            my_list.extend(5)

        self.assertEqual("Values are not iterable", str(ex.exception))

    def test_extend_method(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        extended_list = my_list.extend([5, 6])
        self.assertEqual([1, 2, 3, 5, 6], extended_list)

    def test_insert_method(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)
        my_list.insert(0, 5)

        self.assertEqual([5, 1, 2, 3], my_list._CustomList__elements)

    def test_pop_method(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        value = my_list.pop()
        self.assertEqual(3, value)

    def test_clear_method(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        my_list.clear()

        self.assertEqual([], my_list._CustomList__elements)

    def test_index_method_raises(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        with self.assertRaises(ValueError) as ex:
            my_list.index(6)
        self.assertEqual("6 is not in list", str(ex.exception))

    def test_index_method(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        index = my_list.index(2)
        self.assertEqual(1, index)

    def test_count_method(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)
        count = my_list.count(6)
        self.assertEqual(0, count)

    def test_reverse_method(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        my_list.reverse()
        self.assertEqual([3, 2, 1], my_list._CustomList__elements)

    def test_copy_method(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)
        new_list = my_list.copy()
        self.assertEqual([1, 2 ,3], new_list)


if __name__ == '__main__':
    main()
