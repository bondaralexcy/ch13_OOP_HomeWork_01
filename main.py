from src.classes import Product, Category


if __name__ == '__main__':
    """Проверка работы классов"""


    smartphon_1 = Product("Samsung Galaxy C23 Ultra",
                          "256GB, Серый цвет, 200MP камера",
                          180000.0,
                          5)

    print(smartphon_1.name)

    smartphon_2 = Product.new_product(
        {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      })

    print(smartphon_2.name)

    cat2 = Category("Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [smartphon_1, smartphon_2])


    print(cat2.name)
    print(f"Количество категорий: {cat2.category_count}")
    print(f"Количество продуктов: {cat2.products_count}")



    smartphon_3 = Product.new_product(
        {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Серебристый",
        "price": 32500.0,
        "quantity": 2
      })

    print(smartphon_3.name)
    print(f"Старая цена: {smartphon_3.price}")
    smartphon_3.price = 3000
    print(f"Новая цена: {smartphon_3.price}")

    cat2.add_products(smartphon_3)

    #
    # print(cat2.get_products())
    print(f"Количество категорий: {cat2.category_count}")
    print(f"Количество продуктов: {cat2.products_count}")

    print(cat2.products_list)