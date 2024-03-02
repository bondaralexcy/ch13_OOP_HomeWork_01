
from src.classes import Product

class Smartphone(Product):
    """ Дочерний класс от базового класса Product"""

    def __init__(self, name, description, price, quantity, productivity: str, model: str, memory: str, color: str):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        super().__init__(name, description, price, quantity)
        self.productivity = productivity    # Производительность
        self.model = model                  # Модель
        self.memory = memory                # Память
        self.color = color                  # Цвет



class Garden_grass(Product):
    """ Дочерний класс от базового класса Product"""
    def __init__(self, name, description, price, quantity, country: str, expiration: int, color: str):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        super().__init__(name, description, price, quantity)
        self.country = country  # страна-производитель
        self.expiration = expiration  # срок прорастания
        self.color = color  # Цвет

