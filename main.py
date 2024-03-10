
from src.category import Category, CategoryIter
from src.product import Product
from src.child_classes import Smartphone, Garden_grass, AnyProduct


def common_check():
    #
    # Проверка создания объектов и манипуляции с ними без загрузки из файла json
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
                "price": 150000,
                "quantity": 3,
                "productivity": "20M fps",
                "model": "Note 12",
                "memory": "2048GB",
                "color": "Синий"
            }
        )



    print(smartphon_1)
    # print(len(smartphon_1))
    # print(smartphon_1.get_product_name())
    # print(smartphon_1.get_product_quantity())
    # print(smartphon_1.get_product_description())
    # print(smartphon_1.get_memory())
    #
    print(smartphon_2)
    #
    print(smartphon_3)
    # print(smartphon_3.price)
    # smartphon_3.price = 55000
    # print(smartphon_3.price)

    cat = Category("Смартфоны", "Новые поступления на склад", [smartphon_1, smartphon_2, smartphon_3])
    print(cat)


    # print(len(cat))
    # print(cat.get_name())
    # print(cat.get_description())
    # print(cat.products_list)
    print("Средняя цена смартфона = {:.2f}".format(cat.avg_price()))
    exit()

    print('\nИнициализация объекта Garden_grass')
    Grass1 = Garden_grass("Овсяница красная", "Овсяница красная (Festuca rubra L.) - корневищный и рыхлокустовой низовой многолетний злак, вид травянистых растений семейства злаковых высотой до 60см",
                        500, 1700, "Россия", "1 мес.","Красноватый")

    print('\nДобавление нового продукта Garden_grass')
    Grass2 = Garden_grass.new_product(
            {
            "name": "Райграс многолетний",
            "description": "Райграс пастбищный (Lolium perenne L.) - низовой рыхлокустовой быстроукореняющийся многолетний злак высотой от 15 до 60см.",
            "price": 300,
            "quantity": 400,
            "country": "Россия",
            "expiration": "15 дней",
            "color": "Синий"
            }
        )

    print(Grass2)
    print(len(Grass2))
    print(Grass2.price)
    print(Grass2.get_product_name())
    print(Grass2.get_product_quantity())
    print(Grass2.get_product_description())
    print(Grass2.get_country())


    garden_grass_cat = Category("Трава газонная", "Наличие в магазине", [Grass1])

    print(garden_grass_cat)
    print(len(garden_grass_cat))
    print(garden_grass_cat.get_name())
    print(garden_grass_cat.get_description())
    print(garden_grass_cat.products_list)
    print(f"Количество категорий: {garden_grass_cat.category_count}")
    print(f"Количество продуктов: {garden_grass_cat.products_count}")

    print("Добавляем еще один продукт в категорию garden_grass_cat")

    garden_grass_cat.add_product(Grass2)

    print(f"Количество продуктов: {garden_grass_cat.products_count}")

    tee_cap_1 = AnyProduct(
            "Чайная пара кобальтовая",
            "Чашка чайная и блюдце кобальтовые производства ЛФЗ",
            2700,
            20
        )

    tee_cap_2 = AnyProduct(
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
    # print(tee_set_cat.get_products())

    print(f"Количество категорий: {tee_set_cat.category_count}")
    print(f"Количество продуктов: {tee_set_cat.products_count}")

    print('\nПроверка итерации')
    print(f"Категория: {garden_grass_cat.get_name()}")
    prod_list = CategoryIter(garden_grass_cat)
    for pd in prod_list:
        # print(type(pd)) # При данной загрузке тип pd - объект класса Product
        # print(pd.get('name'))
        print(pd.get_product_name())

    cap = AnyProduct(
            "Чайная пара белая",
            "Чашка чайная и блюдце белые, Китай, для микроволновки",
            700,
            130
        )

    print('\nПроверка сложения объектов')
    print(f'Grass1 + Grass2 = {Grass1 + Grass2}')
    print(f'Smartphon_3 + Smartphon_1 = {smartphon_3 + smartphon_1}')
    # print(f'Smartphon_3 + Grass2 = {smartphon_3 + Grass2}')
    # print(f'Grass1 + cap = {Grass1 + cap}')

def main():
    smartphon_1 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Серебристый",
        32500.0,
        10,
        "10M fps",
        "Note 11",
        "1024GB",
        "Серебристый"
        )

    # print(smartphon_1.get_product_name())
    # print(len(smartphon_1))
    # print(smartphon_1.get_product_quantity())
    # print(smartphon_1.get_product_description())
    # print(smartphon_1.get_memory())

    smartphon_3 = Smartphone.new_product(
            {
                "name": "Xiaomi Redmi Note 12",
                "description": "1024GB, Синий",
                "price": 50000,
                "quantity": 0,
                "productivity": "20M fps",
                "model": "Note 12",
                "memory": "2048GB",
                "color": "Синий"
            }
        )
    # grass = Garden_grass(
    #     "Райграс многолетний",
    #     "Райграс пастбищный (Lolium perenne L.) - низовой рыхлокустовой быстроукореняющийся многолетний злак высотой от 15 до 60см.",
    #     300,
    #     400,
    #     "Россия",
    #     "1 месяц",
    #     "Красноватая"
    #     )
    #
    # cap = AnyProduct(
    #         "Чайная пара белая",
    #         "Чашка чайная и блюдце белые, Китай, для микроволновки",
    #         700,
    #         130
    #     )
    #
    cat = Category("Смартфоны", "Новые поступления на склад", [smartphon_3])
    # print(cat)
    # cat.add_product(smartphon_1)
    # print(cat)


def check_order():
    # Создание новой пустой категории
    new_cat = Category.create({"name": "Cмартфоны", "description": "Новые поступления на склад"})
    print(new_cat)
    print(new_cat.products_list)
    print(f"Количество категорий: {new_cat.category_count}")
    print(f"Количество продуктов: {new_cat.products_count}")

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

    new_cat.add_product(smartphon_3)
    print(new_cat)

if __name__ == '__main__':
    """
        Проверка работы классов
    """
    # main()
    # common_check()
    check_order()

