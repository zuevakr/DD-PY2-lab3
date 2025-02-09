class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def get_name(self):
        return self._name

    def set_name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Название должно быть строкой")
        self._name = value

    def get_author(self):
        return self._author

    def set_author(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Автор должен быть строкой")
        self._author = value

    def __str__(self):
        return f"Книга {self.get_name()}. Автор {self.get_author()}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    def get_pages(self):
        return self._pages

    def set_pages(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self._pages = value

    def __str__(self):
        return f"Книга {self.get_name()}. Автор {self.get_author()}. Страниц: {self.get_pages()}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r}, pages={self.get_pages()!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def get_duration(self):
        return self._duration

    def set_duration(self, value: float):
        if not isinstance(value, float) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом с плавающей запятой")
        self._duration = value

    def __str__(self):
        return f"Книга {self.get_name()}. Автор {self.get_author()}. Длительность: {self.get_duration()} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r}, duration={self.get_duration()!r})"