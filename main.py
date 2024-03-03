
from src.classes import Category, Product, CategoryIter
from src.child_classes import Smartphone, Garden_grass


def check_classes():
    #
    # Проверки без загрузки из файла json
    #

    smartphon_1 = Smartphone(
            "Xiaomi Redmi Note 11",
            "1024GB, Серебристый",
            32500.0,
            2,
            "10M fps",
            "Note 11",
            "1024GB",
            "Серебристый"
        )

    smartphon_2 = Smartphone(
        "Xiaomi Redmi Note 9",
        "512GB, Серебристый",
        20500.0,
        5,
        "2M fps",
        "Note 9",
        "512GB",
        "Серебристый"
        )

    smartphon_3 = Smartphone.new_product(
            {
                "name": "Xiaomi Redmi Note 12",
                "description": "1024GB, Синий",
                "price": 50000,
                "quantity": 3,
                "productivity": "20M fps",
                "model": "Note 12",
                "memory": "2048GB",
                "color": "Синий"
            }
        )



    # print(smartphon_1)
    # print(len(smartphon_1))
    # print(smartphon_1.get_product_name())
    # print(smartphon_1.get_product_quantity())
    # print(smartphon_1.get_product_description())
    # print(smartphon_1.get_memory())
    #
    # print(smartphon_2)
    #
    # print(smartphon_3)
    # print(smartphon_3.price)
    # smartphon_3.price = 55000
    # print(smartphon_3.price)

    cat = Category("Смартфоны", "Новые поступления на склад", [smartphon_1, smartphon_2])
    print(cat)
    print(len(cat))
    print(cat.get_name())
    print(cat.get_description())
    print(cat.products_list)


    Grass1 = Garden_grass("Овсяница красная", "Овсяница красная (Festuca rubra L.) - корневищный и рыхлокустовой низовой многолетний злак, вид травянистых растений семейства злаковых высотой до 60см",

                        500, 1700, "Россия", "1 мес.","Красноватый")

    Grass2 = Garden_grass.new_product(
            {
            "name": "Райграс многолетний",
            "description": "Райграс пастбищный (Lolium perenne L.) - низовой рыхлокустовой быстроукореняющийся многолетний злак высотой от 15 до 60см.",
            "price": 300,
            "quantity": 400,
            "country": "Россия",
            "expiration": "Note 12",
            "color": "Синий"
            }
        )

    # print(Grass2)
    # print(len(Grass2))
    # print(Grass2.price)
    # print(Grass2.get_product_name())
    # print(Grass2.get_product_quantity())
    # print(Grass2.get_product_description())
    # print(Grass2.get_country())

    garden_grass_cat = Category("Трава газонная", "Наличие в магазине", [Grass1, Grass2])

    print(garden_grass_cat)
    print(len(garden_grass_cat))
    print(garden_grass_cat.get_name())
    print(garden_grass_cat.get_description())
    print(garden_grass_cat.products_list)

    print(f"Количество категорий: {garden_grass_cat.category_count}")
    print(f"Количество продуктов: {garden_grass_cat.products_count}")

    tee_cap_1 = Product(
            "Чайная пара кобальтовая",
            "Чашка чайная и блюдце кобальтовые производства ЛФЗ",
            2700,
            20
        )

    tee_cap_2 = Product(
            "Чайная пара белая",
            "Чашка чайная и блюдце белые, Китай, для микроволновки",
            700,
            130
        )

    print(tee_cap_2)
    print(len(tee_cap_2))
    print(tee_cap_2.get_product_name())
    print(tee_cap_2.get_product_quantity())
    print(tee_cap_2.get_product_description())

    tee_set_cat = Category("Чайные_наборы", "Чайные наборы в наличии", [tee_cap_2, tee_cap_1])

    print(tee_set_cat)
    print(len(tee_set_cat))
    print(tee_set_cat.get_name())
    print(tee_set_cat.get_description())
    print(tee_set_cat.products_list)
    print(tee_set_cat.get_products())

    print(f"Количество категорий: {tee_set_cat.category_count}")
    print(f"Количество продуктов: {tee_set_cat.products_count}")

    print('\nПроверка итерации')
    print(f"Категория: {tee_set_cat.get_name()}")
    prod_list = CategoryIter(tee_set_cat)
    for pd in prod_list:
        print(pd.get_product_name())


if __name__ == '__main__':
    """
        Проверка работы классов
    """
    # main()
    check_classes()


# from src.utils import load_data
# def main():
    # """
    # Загружаем данные из json-файла products.json
    # Инициализируем экземпляры классов Category и Product
    # Проверяем работу методов классов
    # :return:
    # """
    # data = load_data('products.json')
    # i = 1
    # j = 1
    # # Цикл по категориям
    # for unit in data:
    #     # Список продуктов данной категории
    #     list_product = [un for un in unit["products"]]
    #     # Создаем объекты класса Category. Присваиваем их переменным category_1, category_2
    #     locals()[f'category_{i}'] = Category(unit["name"], unit["description"], unit["products"])
    #     print(f'++++++++++++++ category_{i} ++++++++++++++')
    #     # Проверка метода __len__
    #     print(f'Количество классов Product в категории: {len(locals()[f"category_{i}"])}')
    #     # Проверка метода __str__
    #     print(locals()[f'category_{i}'])
    #     i += 1
    #
    #     for element in list_product:
    #         # Создаем объекты класса Product. Присваиваем их переменным product_1, product_2 итд
    #         locals()[f'product_{j}'] = Product(element["name"], element["description"], element["price"], element["quantity"])
    #         print(f'------------ product_{j} -----------------')
    #         # Проверка метода __len__
    #         print(f'Количество продуктов на складе: {len(locals()[f"product_{j}"])}')
    #         # Проверка метода __str__
    #         print(locals()[f'product_{j}'])
    #         j += 1
    #
    # # Проверяем работу методов классов
    # print('\nПроверка итерации')
    # prod_list = CategoryIter(locals()[f'category_{1}'])
    # for pd in prod_list:
    #     print(pd.get_product_name())
    #
    # print('\nПроверка сложения объектов')
    # print(f'product_1 + product_2 = {locals()['product_1'] + locals()['product_2']}')
    #
    # print('\nПроверка декоратора price')
    # print(f"Старая цена: {locals()['product_2'].price}")
    # locals()['product_2'].price = 30000
    # print(f"Новая цена: {locals()['product_2'].price}")
    #
