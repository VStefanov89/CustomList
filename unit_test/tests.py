from unittest import TestCase, main
from custom_list.lists import CustomList


class CustomListTest(TestCase):
    def test_append_method_and_return_list(self):
        my_list = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], my_list._CustomList__elements)

        my_list.append(4)
        self.assertEqual([1, 2, 3, 4], my_list._CustomList__elements)


if __name__ == '__main__':
    main()
