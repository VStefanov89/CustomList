class CustomList:
    def __init__(self, *args):
        self.__elements = []
        for el in args:
            self.__elements.append(el)

    def append(self, value):
        self.__elements.append(value)

    def remove(self, index):
        try:
            element = self.__elements.pop(index)
            return element
        except IndexError:
            raise IndexError("Index out of range")
        except TypeError:
            raise ValueError("Index is not a valid integer")

    def get(self, index):
        try:
            value = self.__elements[index]
            return value
        except IndexError:
            raise IndexError("Index out of range")

    def extend(self, values):
        try:
            self.__elements.extend(values)
            return self.__elements
        except TypeError:
            raise ValueError("Values are not iterable")

    def insert(self, index, value):
        self.__elements.insert(index, value)

    def pop(self):
        value = self.__elements.pop()
        return value

    def clear(self):
        self.__elements.clear()

    def index(self, value):
        try:
            index = self.__elements.index(value)
            return index
        except ValueError:
            raise ValueError(f"{value} is not in list")

    def count(self, value):
        return self.__elements.count(value)

    def reverse(self):
        return self.__elements.reverse()

    def copy(self):
        new_list = self.__elements.copy()
        return new_list




    def __str__(self):
        result = ", ".join([str(el) for el in self.__elements])
        return f"[{result}]"



my_list = CustomList(1, 2, 3)
print(my_list)