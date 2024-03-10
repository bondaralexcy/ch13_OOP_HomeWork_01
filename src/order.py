from src.category import BaseCategory, ZeroQuantityError
from src.product import Product


class Order(BaseCategory):
    """
        Класс заказа продуктов
        Доп. задание к уроку 15.2
        Создать класс «Заказ», в котором будет ссылка на то, какой товар был куплен,
        количество купленного товара, а также итоговая стоимость.
        В заказе может быть указан только один товар.
    """

    name: str
    description: str
    __products: list

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляра класса Category. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = []  # Пустой список продуктов
        #Добавляем в список только первый продукт из входного списка
        if len(products) > 0:
            self.add_product(products[0])
            print(f'Создан заказ: {self.name} Добавлен продукт: {products[0]["name"]}')
        else:
            print(f'Создан пустой заказ: {self.name}')

    @classmethod
    def create(cls, value):
        """ Создание нового пустого Заказа
        :param name: Наименование Заказа
        :param description: Описание
        """
        name, description = (value["name"], value["description"])
        products = []
        return cls(name, description, products)


    def __str__(self):
        # Название Заказа, наименование Продукта
        if len(self) > 0:
            return f'Класс: {__class__.__name__}  Наименование Заказа: {self.name}, Продукт: {self.__products[0].get_product_name()} шт.'
        else:
            return f'Класс: {__class__.__name__}  Наименование Заказа: {self.name}, Заказ пустой'

    def __len__(self):
        # Длина определена как количество продуктов в Заказе
        return len(self.get_products())

    def get_name(self):
        """ Наименование Заказа"""
        return self.name

    def get_description(self):
        """ Описание Заказа"""
        return self.description

    def get_products(self) -> list:
        "Возвращает список продуктов в Заказе"" """
        return self.__products

    def add_product(self, value):
        """Метод добавляет продукт в список продуктов  Заказа
            Доработан по требованию задания 15.1 так, чтобы не было возможности добавить
            вместо продукта или его наследников любой другой объект"""
        if not isinstance(value, Product):
            raise TypeError("Добавлять в Заказ можно только объекты класса Product и его наследников")
        # В заказе может быть только один товар
        if len(self) > 0:
            print(f"Попытка добавить еще один товар в {self.get_name()}\nВ заказе уже есть товар '{self.__products[0].get_product_name()}'")
            exit()

        # Обрабатываем ситуацию с нулевым количеством товара
        try:
            if value.quantity == 0:
                raise ZeroQuantityError
        except ZeroQuantityError as e:
            e.message = "Tовар с нулевым количеством не может быть добавлен в Заказ"
            print(e)
        else:
            self.__products.append(value)
            print(f'Товар "{value.name}" добавлен в Заказ "{self.name}"')
        finally:
            print("Обработка добавления товара в Заказ завершена")
