from src.item import Item


class MixinLang:
    language = "EN"

    @classmethod
    def change_language(cls) -> str:
        """Метод меняющий раскладку клавиатуры"""
        if cls.language == "EN":
            cls.language = "RU"
        else:
            cls.language = "EN"
        return cls.language


class Keyboard(Item, MixinLang):
    def __init__(
        self, name: str, price: float, quantity: int, language: str = MixinLang.language
    ):
        """
        Создание экземпляра класса Keyboard дочерний от Item
        :param name: Название клавиатуры.
        :param price: Цена за одну клавиатуру.
        :param quantity: Количество клавиатур в магазине.
        :param language: Раскладка клавиатуры
        """
        super().__init__(name, price, quantity)
        self.__language = language

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__language})"

    @property
    def language(self) -> str:
        """Геттер для приватного атрибута language"""
        return self.__language

    def change_lang(self) -> None:
        """Метод меняющий раскладку на основе метода описанного в классе MixinLang"""
        self.__language = MixinLang.change_language()
