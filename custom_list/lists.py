class CustomList:
    def __init__(self, *args):
        self.__elements = []
        for el in args:
            self.__elements.append(el)

    def __str__(self):
        result = ", ".join([str(el) for el in self.__elements])
        return f"[{result}]"

