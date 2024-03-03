from src.utils import load_data
from src.classes import Category, Product, CategoryIter

    # Загружаем данные из json-файла products.json
    # Инициализируем экземпляры классов Category и Product
    # Проверяем работу методов классов"

data = load_data('products.json')
# print(data)


i = 1
j = 1
# Цикл по категориям
for unit in data:
    # Список продуктов данной категории
    list_product = [un for un in unit["products"]]
    # Создаем объекты класса Category. Присваиваем их переменным category_1, category_2
    locals()[f'category_{i}'] = Category(unit["name"], unit["description"], unit["products"])
    print(f'++++++++++++++ category_{i} ++++++++++++++')
    # Проверка метода __len__
    print(f'Количество классов Product в категории: {len(locals()[f"category_{i}"])}')
    # Проверка метода __str__
    print(locals()[f'category_{i}'])
    i += 1

    for element in list_product:
        # Создаем объекты класса Product. Присваиваем их переменным product_1, product_2 итд
        locals()[f'product_{j}'] = Product(element["name"], element["description"], element["price"], element["quantity"])
        print(f'------------ product_{j} -----------------')
        # Проверка метода __len__
        print(f'Количество продуктов на складе: {len(locals()[f"product_{j}"])}')
        # Проверка метода __str__
        print(locals()[f'product_{j}'])
        j += 1

# Проверяем работу методов классов
print('\nПроверка итерации')
prod_list = CategoryIter(locals()[f'category_{1}'])
for pd in prod_list:
    # print(type(pd))   # При данной загрузке тип pd - словарь
    print(pd.get('name'))

print('\nПроверка сложения объектов')
print(f'product_1 + product_2 = {locals()['product_1'] + locals()['product_2']}')

print('\nПроверка декоратора price')
print(f"Старая цена: {locals()['product_2'].price}")
locals()['product_2'].price = 30000
print(f"Новая цена: {locals()['product_2'].price}")

