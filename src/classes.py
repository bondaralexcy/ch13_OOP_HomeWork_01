class Category:
    """
        Класс категории продуктов
    """
    category_count = 0  # Общее количество категорий
    products_count = 0  # Общее количество униклальных продуктов, без учета количества их в наличии

    name: str
    description: str
    products: list

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.products_count += len(products)

    def __str__(self):
        return f'Класс: {__class__.__name__} \n  {self.name} \n  {self.description} \n  Количество: {Category.products_count}'

    def __len__(self):
        return Category.products_count

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_products(self):
        return self.__products

    def add_products(self, value):
        """Метод добавляет продукт в список продуктов __products"""
        self.__products.append(value)
        Category.products_count += 1

    @property
    def products_list(self):
        """Геттер, который выводит список товаров в заданном формате"""
        list_product = []
        for product in self.__products:
            list_product.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
        return "".join(list_product)



class Product:
    """
        Класс Product
    """
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

    def __str__(self):
        return f'Класс: {__class__.__name__} \n  {self.name} \n  {self.description} \n  Цена: {self.price} \n  Количество: {self.quantity}'

    def __len__(self):
        return self.quantity

    def __add__(self, other):
        return self.quantity + other.quantity


    def get_product_name(self):
        return self.name

    def get_product_description(self):
        return self.description

    def get_product_quantity(self):
        return self.quantity

    @classmethod
    def new_product(cls, value):
        """Метод класса создает и возвращает новый продукт
            value - словарь типа:
             {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Серебристый",
            "price": 32500.0,
            "quantity": 2
            }
        """
        name, description, price, quantity = (value["name"], value["description"], value["price"], value["quantity"])
        return cls(name, description, price, quantity)

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

