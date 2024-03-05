
from src.product import Product

class Smartphone(Product):
    """ Дочерний класс от базового класса Product"""

    def __init__(self, name, description, price, quantity, productivity: str, model: str, memory: str, color: str):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        super().__init__(name, description, price, quantity)
        self.productivity = productivity    # Производительность
        self.model = model                  # Модель
        self.memory = memory                # Память
        self.color = color                  # Цвет

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


    # Добавляем особые методы для данной категории продуктов
    def get_productivity(self):
        return self.productivity

    def get_model(self):
        return self.model

    def get_memory(self):
        return self.memory

    def get_color(self):
        return self.color






class Garden_grass(Product):
    """ Дочерний класс от базового класса Product"""
    def __init__(self, name, description, price, quantity, country: str, expiration: int, color: str):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        super().__init__(name, description, price, quantity)
        self.country = country  # страна-производитель
        self.expiration = expiration  # срок прорастания
        self.color = color  # Цвет

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
        name, description, price, quantity, country, expiration, color = (
                value["name"], value["description"], value["price"], value["quantity"],
                value["country"], value["expiration"], value["color"]
                )
        return cls(name, description, price, quantity, country, expiration, color)

    # Добавляем особые методы для данной категории продуктов
    def get_country(self):
        return self.country

    def get_expiration(self):
        return self.expiration


    def get_color(self):
        return self.color