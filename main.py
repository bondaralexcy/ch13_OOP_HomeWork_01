from src.classes import Product, Category


if __name__ == '__main__':
    """Проверка работы классов"""

    product1 = Product("Киви", "Только у нас", 10, 100)
    product2 = Product("Белый налив", "Ранний сорт", 150, 1000)

    cat1 = Category("Фрукты", "Лучшие фрукты на рынке", [product1.name, product2.name])

    print(cat1.name)
    print(cat1.descr)
    print(cat1.products)

    print(cat1.category_count)
    print(cat1.products_count)


    cat2 = Category("Смартфоны", "Только у нас", ['Samsung Galaxy C23 Ultra'])
    print(cat2.name)
    print(cat2.products)

    print(cat2.category_count)
    print(cat2.products_count)