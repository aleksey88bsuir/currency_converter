from typing import List, Union, Any


AddAbr = Union[str, List[str]]


class CursAbrIter:
    def __init__(self, data: List[str]) -> None:
        self.__data = self.__load_data_in_var(data)

    @property
    def data(self) -> AddAbr:
        return self.__data

    @data.setter
    def data(self, new_data: List[str]) -> None:
        if self.__validate(new_data):
            self.__data = new_data

    @staticmethod
    def __validate(set_of_data: Any) -> bool:
        return isinstance(set_of_data, list) and len(set_of_data) > 0 and \
            all(isinstance(obj_, str) for obj_ in set_of_data)

    def __load_data_in_var(self, data: List[str]):
        if self.__validate(data):
            return data
        else:
            raise ValueError('Неверные входные данные')

    def __validate_adding_data(self, some_data):
        if not isinstance(some_data, (list, str)):
            raise ValueError('Должно передаваться AddAbr')
        if isinstance(some_data, list):
            if not all(isinstance(data, str) for data in some_data):
                raise ValueError('В списке должны быть строки')

    def add_new_abr(self, new_abr: AddAbr) -> None:
        self.__validate_adding_data(new_abr)
        if isinstance(new_abr, list):
            self.data.extend(new_abr)
        elif new_abr not in self.data:
            self.data.append(new_abr)

    def __iter__(self) -> object:
        self.index = 0
        return self

    def __next__(self) -> str:
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
        else:
            raise StopIteration()
        return result
