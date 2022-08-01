class CustomList:
    def __init__(self, *args):
        self.__elements = []
        for el in args:
            self.__elements.append(el)

    def append(self, value):
        self.__elements.append(value)

    def __str__(self):
        result = ", ".join([str(el) for el in self.__elements])
        return f"[{result}]"

my_list = CustomList(1, 2, 3)

print(my_list._CustomList__elements)