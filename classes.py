from dataclasses import dataclass


@dataclass()
class My_Exception(Exception):
    exc: str


@dataclass
class Candidate:
    """
    Класс кандидата, создает объекты используя данные из JSON
    """
    id: int
    name: str
    picture: str
    position: str
    gender: str
    age: int
    skills: str


@dataclass()
class PaginationHelper:
    """
    Класс для пагинации страниц
    """
    # список отображаемых элементов
    collections: list
    # количество элементов на странице
    item_per_page: int

    def items_count(self) -> int:
        """
        Возвращает общее количество элементов
        :return: int
        """
        return len(self.collections)

    def page_count(self) -> int:
        """
        Возвращает количество страниц
        :return: int
        """
        if self.items_count() % self.item_per_page == 0:
            return int(self.items_count() / self.item_per_page)
        else:
            return int(self.items_count() // self.item_per_page + 1)

    def items_page(self, page) -> list:
        """
        возвращает список элементов которые будут отображаться на страничке page
        :param page: номер запрашиваемой страницы
        :return:list
        """
        if page in range(self.items_count() + 1):
            start_index_item: int = self.item_per_page * (page - 1)
            end_index_item: int = start_index_item + self.item_per_page
            return self.collections[start_index_item:end_index_item]
        else:
            raise My_Exception("Такой страницы нет")
