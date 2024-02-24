
from src.classes import Category, Product
from src.utils import load_data
def main():
    """
    Загружаем данные из json-файла products.json
    Инициализируем экземпляры классов Category и Product
    Проверяем работу методов классов
    :return:
    """
    data = load_data('products.json')
    i = 1
    j = 1
    # Цикл по категориям
    for unit in data:
        # Список продуктов данной категории
        list_product = [un for un in unit["products"]]
        # Создаем объекты класса Category. Присваиваем их переменным category_1, category_2
        locals()[f'category_{i}'] = Category(unit["name"], unit["description"], unit["products"])
        print(f'++++++++++++++ category_{i} ++++++++++++++')
        print(len(locals()[f'category_{i}']))
        print(locals()[f'category_{i}'])
        i += 1

        for element in list_product:
            # Создаем объекты класса Product. Присваиваем их переменным product_1, product_2 итд
            locals()[f'product_{j}'] = Product(element["name"], element["description"], element["price"], element["quantity"])
            print(f'------------ product_{j} -----------------')
            print(len(locals()[f'product_{j}']))
            print(locals()[f'product_{j}'])
            j += 1

    # Проверяем работу методов классов
    print(f'product_1 + product_2 = {locals()['product_1'] + locals()['product_2']}')
    print(f"Старая цена: {locals()['product_2'].price}")
    locals()['product_2'].price = 30000
    print(f"Новая цена: {locals()['product_2'].price}")


if __name__ == '__main__':
    """
        Проверка работы классов
    """
    main()

    #
    # Проверки без загрузки из файла json
    #
    # print(len(smartphon_2))
    #
    # cat2 = Category("Смартфоны",
    #     "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    #     [smartphon_1, smartphon_2])
    #
    # print(cat2)
    # print(len(cat2))
    #
    # print(f"Количество категорий: {cat2.category_count}")
    # print(f"Количество продуктов: {cat2.products_count}")
    #
    #
    # smartphon_3 = Product.new_product(
    #     {
    #     "name": "Xiaomi Redmi Note 11",
    #     "description": "1024GB, Серебристый",
    #     "price": 32500.0,
    #     "quantity": 2
    #   })
    #
    # print(f'smartphon_3 {smartphon_3}')
    #
    # print(f'smartphon_2 + smartphon_3 = {smartphon_2 + smartphon_3}')
    #
    #
    # print(f"Старая цена: {smartphon_3.price}")
    # smartphon_3.price = 3000
    # print(f"Новая цена: {smartphon_3.price}")
    #
    # cat2.add_products(smartphon_3)
    #
    # #
    # # print(cat2.get_products())
    # print(f"Количество категорий: {cat2.category_count}")
    # print(f"Количество продуктов: {cat2.products_count}")
    #
    # print(cat2.products_list)