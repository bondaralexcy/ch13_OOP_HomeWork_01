from src.product import Product


class Category:
    """
        Класс категории продуктов
    """
    category_count = 0  # Общее количество категорий
    products_count = 0  # Общее количество униклальных продуктов, без учета количества их в наличии

    name: str
    description: str
    __products: list

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляра класса Category. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = []    # Пустой список объектов класса Product
        # self.__products = products  # Список объектов класса Product
        for product in products:
            self.add_product(product)

        Category.category_count += 1
        # Category.products_count += len(products)

    def __str__(self):
        #Название категории, количество продуктов: 200 шт.
        return f'Класс: {__class__.__name__} \n  {self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        # Длина определена как количество объектов в данной категории товаров
        return len(self.get_products())


    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_products(self) -> list:
        # Возвращает список продуктов, сохраненных в данной категории
        return self.__products


    def add_product(self, value):
        """Метод добавляет продукт в список продуктов __products
            Доработан по требованию задания 15.1 чтобы не было возможности добавить
            вместо продукта или его наследников любой другой объект"""
        if not isinstance(value, Product):
            raise TypeError("Добавлять можно только объекты класса Product и его наследников")
        # Обрабатываем ситуацию с нулевым количеством товара
        try:
            if value.quantity == 0:
                raise MyValueError
        except MyValueError as e:
            e.message = "Tовар с нулевым количеством не может быть добавлен"
            print(e)
        else:
            self.__products.append(value)
            Category.products_count += 1
            print(f'Товар "{value.name}" добавлен в категорию "{self.name}"')
        finally:
            print("Обработка добавления товара завершена")


        # Этот код остался от выполнения задания №1
        #
        # if value.quantity == 0:
        #     raise ValueError("Tовар с нулевым количеством не может быть добавлен")
        #
        # else:
        #     self.__products.append(value)
        #     Category.products_count += 1

    @property
    def products_list(self):
        """Геттер, который выводит список товаров в заданном формате"""
        list_product = []
        for product in self.__products:
            list_product.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
        return "".join(list_product)

    def avg_price(self):
        """
            Метод подсчитывает средний ценник всех товаров.
            С помощью исключений обработать случай, когда в категории нет товаров
            и сумма всех товаров будет делиться на ноль.
            В случае, если такое происходит, возвращать ноль.
        """
        total_sum = 0
        total_quant = 0
        try:
            for product in self.__products:
                total_sum += product.price * product.quantity
                total_quant += product.quantity
            return total_sum / total_quant
        except ZeroDivisionError:
            return 0

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


class MyValueError(Exception):
    """ Пользовательский класс обработки исключения """
    message = ""
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Что-то не так с параметрами объекта'

    def __str__(self):
        return self.message

