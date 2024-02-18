class Category:
    """Класс для представления категории продукта"""
    category_count = 0  # Общее количество категорий
    products_count = 0  # Общее количество униклальных продуктов, без учета количества их в наличии

    name: str
    descr: str
    products: list

    def __init__(self, name: str, descr: str, products: list):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.descr = descr

        # Список объектов класса Product

        self.products = products

        Category.category_count += 1
        Category.products_count += len(products)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.descr

    def get_products(self):
        return self.products


class Product:
    """Класс продукт"""
    name: str
    descr: str
    price: float
    quantity: int
    """Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра."""

    def __init__(self, name, descr, price, quantity):
        self.name = name
        self.descr = descr
        self.price = price
        self.quantity = quantity

    def get_product_name(self):
        return self.name

    def get_product_description(self):
        return self.descr

    def get_product_price(self):
        return self.price

    def get_product_quantity(self):
        return self.quantity

