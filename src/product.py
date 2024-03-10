from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ Абстрактный общий класс для всех продуктов"""

    # Определяем абстрактный метод класса
    @classmethod
    @abstractmethod
    def new_product(cls, value):
        pass

    # Определяем абстрактный метод
    @abstractmethod
    def get_product_name(self):
        pass


class MixinRepr:
    """ Миксин-класс для вывода информации на консоль о том, что был создан объект. """

    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        # логика с использованием self.__dict__.items()
        attrs = ', '.join([f"{attr}={getattr(self, attr)}" for attr in self.__dict__])
        return f"Создан объект: {self.__class__.__name__} ({attrs})"


class Product(BaseProduct):
    """ Класс Product - родительский класс для остальных продуктов """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра.
            Для атрибута price создал геттер и сеттер, поэтому переопределил его как защищенный
        """

        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f'Класс: {__class__.__name__} \n  {self.name},  {self.price} руб.  Остаток: {self.quantity}'

    def __len__(self):
        return self.quantity

    def __add__(self, other):
        """
        Результат выполнения сложения двух продуктов - сложение сумм, умноженных на количество на складе
        Доработать функционал сложения таким образом, чтобы можно было складывать товары только из одинаковых классов продуктов.
        То есть если складывать товар класса «Смартфон» и товар класса «Продукт», то должна быть ошибка типа.
        """
        # Если использовать эту проверку, то ее достаточно сделать в классе Product
        # Однако сравнивать типы почему-то не рекомендуется
        # if not (type(self) == type(other)):
        #     raise TypeError("Складывать можно объекты только из одной категории товаров")

        # Другой вариант
        # Здесь проверяется принадлежность объекта классу Product и его наследникам
        # Аналогичная проверка реализована в дочерних классах Smartphone и GardenGrass
        # При такой реализации условие задачи выполняется:
        #    если складывать товар класса «Смартфон» и товар класса «Продукт», то должна возникает ошибка типа.
        #    однако ошибки не возникает если складывать товар класса «Продукт» и товар класса «Смартфон»

        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Складывать можно объекты только из одной категории товаров")


    def get_product_name(self):
        return self.name

    def get_product_description(self):
        return self.description

    def get_product_quantity(self):
        return self.quantity

    @classmethod
    def new_product(cls, value: dict):
        """Метод класса создает и возвращает новый продукт
            value - словарь типа:
             {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Серебристый",
            "price": 32500.0,
            "quantity": 2
            }
        """
        # name, description, price, quantity = (value["name"], value["description"], value["price"], value["quantity"])
        # return cls(name, description, price, quantity)
        return cls(**value)


    @property
    def price(self):
        """геттер для атрибута цены"""
        return self._price

    @price.setter
    def price(self, value):
        """сеттер для атрибута цены с проверкой значения"""
        if value <= 0:
            print("Цена введена не корректно")
        elif value < self._price:
            while True:
                answer = input("Новая цена меньше, чем старая. Вы уверены что хотите изменить цену? (y/n): ")
                if answer.lower() == "y":
                    self._price = value
                    break
                elif answer.lower() == "n":
                    # self.price = self.price
                    break
        else:
            self._price = value

