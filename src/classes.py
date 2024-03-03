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
        #Название категории, количество продуктов: 200 шт.
        return f'Класс: {__class__.__name__} \n  {self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        # return Category.products_count
        return len(self.get_products())


    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_products(self) -> list:
        return self.__products


    def add_product(self, value):
        """Метод добавляет продукт в список продуктов __products
            Доработан по требованию задания 15.1 чтобы не было возможности добавить
            вместо продукта или его наследников любой другой объект"""
        if not isinstance(value, Product):
            raise TypeError("Добавлять можно только объекты класса Product и его наследников")

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
        return f'Класс: {__class__.__name__} \n  {self.name},  {self.price} руб.  Остаток: {self.quantity}'

    def __len__(self):
        return self.quantity

    def __add__(self, other):
        # результат выполнения сложения двух продуктов - сложение сумм, умноженных на количество на складе
        # Доработать функционал сложения таким образом, чтобы можно было складывать товары только из одинаковых классов продуктов.
        # То есть если складывать товар класса «Смартфон» и товар класса «Продукт», то должна быть ошибка типа.

        if not (type(self) == type(other)):
            raise TypeError("Складывать можно объекты только из одной категории товаров")

        return self.price * self.quantity + other.price * other.quantity


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



class CategoryIter:
    """
    Класс итерации продуктов в заданной категории
    """
    ctg: Category
    def __init__(self, ctg):
        self.ctg = ctg
    def __iter__(self):
        self.stop_num = len(self.ctg)
        self.cur_value = -1
        self.product_list = []
        # Записываем все объекты данной категории в список product_list
        self.product_list = self.ctg.get_products()
        return self

    def __next__(self):
        if self.cur_value + 1 < self.stop_num:
            self.cur_value += 1
            return self.product_list[self.cur_value]
        else:
            raise StopIteration



