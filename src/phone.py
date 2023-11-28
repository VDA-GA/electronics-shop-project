from src.item import Item


class Phone(Item):
    """
        Класс телефонов, дочерний от класса Item.
        """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
               Создание экземпляра класса Phone.

               :param name: Название телефона.
               :param price: Цена за один телефон.
               :param quantity: Количество телефонов в магазине
               :param number_of_sim: Количество сим-карт в телефоне.
               """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __str__(self):
        return self.name

    @property
    def number_of_sim(self) -> int:
        """ Геттер для приватного атрибута number_of_sim"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int) -> None:
        """ Сеттер для приватного атрибута number_of_sim
        Проверяет число сим-карт, если меньше нуля или не целое вызывает ошибку"""
        if number_of_sim <= 0 or type(number_of_sim) is float:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = number_of_sim

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и Phone')
        return self.quantity + other.quantity
