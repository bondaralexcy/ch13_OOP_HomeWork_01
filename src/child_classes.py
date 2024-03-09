
from src.product import Product, MixinRepr

class Smartphone(Product, MixinRepr):
    """ Дочерний класс от базового класса Product"""

    def __init__(self, name, description, price, quantity, productivity: str, model: str, memory: str, color: str):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.productivity = productivity    # Производительность
        self.model = model                  # Модель
        self.memory = memory                # Память
        self.color = color                  # Цвет
        # Вызов  super().__init__ перенесен в конец, чтобы перед миксином были сформированы все атрибуты объекта
        super().__init__(name, description, price, quantity)
    @classmethod
    def new_product(cls, value: dict):
        """Метод класса создает и возвращает новый продукт в категории Cмартфон
            value - словарь типа:
             {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Серебристый",
            "price": 32500.0,
            "quantity": 2
            "productivity": "10M fps",
            "model": "Note 11",
            "memory": "1024GB",
            "color": "Серебристый"
            }
        """
        name, description, price, quantity, productivity, model, memory, color = (
                value["name"], value["description"], value["price"], value["quantity"],
                value["productivity"], value["model"], value["memory"], value["color"]
                )
        return cls(name, description, price, quantity, productivity, model, memory, color)

    def __str__(self):
        return f'Класс: {__class__.__name__} \n  {self.name},  {self.price} руб.  Остаток: {self.quantity}'

    def __add__(self, other):
        # результат выполнения сложения двух продуктов - сложение сумм, умноженных на количество на складе
        # Доработать функционал сложения таким образом, чтобы можно было складывать товары только из одинаковых классов продуктов.
        # То есть если складывать товар класса «Смартфон» и товар класса «Продукт», то должна быть ошибка типа.

        if isinstance(other, Smartphone):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Складывать можно объекты только из одной категории товаров")


    # Добавляем особые методы для данной категории продуктов
    def get_productivity(self):
        return self.productivity

    def get_model(self):
        return self.model

    def get_memory(self):
        return self.memory

    def get_color(self):
        return self.color



class Garden_grass(Product, MixinRepr):
    """ Дочерний класс от базового класса Product"""
    def __init__(self, name, description, price, quantity, country: str, expiration: int, color: str):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.country = country  # страна-производитель
        self.expiration = expiration  # срок прорастания
        self.color = color  # Цвет
        super().__init__(name, description, price, quantity)
    @classmethod
    def new_product(cls, value: dict):
        """Метод класса создает и возвращает новый продукт в категории Газонная травав
            value - словарь типа:
             {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Серебристый",
            "price": 32500.0,
            "quantity": 2
            "productivity": "10M fps",
            "model": "Note 11",
            "memory": "1024GB",
            "color": "Серебристый"
            }
        """
        # name, description, price, quantity, country, expiration, color = (
        #         value["name"], value["description"], value["price"], value["quantity"],
        #         value["country"], value["expiration"], value["color"]
        #         )
        # return cls(name, description, price, quantity, country, expiration, color)

        return cls(**value)   # Можно так?

    def __str__(self):
        return f'Класс: {__class__.__name__} \n  {self.name},  {self.price} руб.  Остаток: {self.quantity}'

    def __add__(self, other):
        # результат выполнения сложения двух продуктов - сложение сумм, умноженных на количество на складе
        # Доработать функционал сложения таким образом, чтобы можно было складывать товары только из одинаковых классов продуктов.
        # То есть если складывать товар класса «Смартфон» и товар класса «Продукт», то должна быть ошибка типа.

        if isinstance(other, Garden_grass):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Складывать можно объекты только из одной категории товаров")

    # Добавляем особые методы для данной категории продуктов
    def get_country(self):
        return self.country

    def get_expiration(self):
        return self.expiration


    def get_color(self):
        return self.color


class AnyProduct(Product, MixinRepr):
    """ Дочерний класс от базового класса Product для произвольной категории продуктов"""

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра.

        """
        super().__init__(name, description, price, quantity)