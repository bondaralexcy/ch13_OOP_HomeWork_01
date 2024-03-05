import pytest

from src.category import Category, Product
from src.child_classes import Smartphone, Garden_grass

@pytest.fixture
def class_category():
    return Category('Смартфоны',
                    'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
                    [dict(name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера",
                          price=180000.0, quantity=5)])


def test_category_init(class_category):
    assert class_category.name == 'Смартфоны'
    assert class_category.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert class_category.get_products() == [
            dict(name="Samsung Galaxy C23 Ultra",
             description="256GB, Серый цвет, 200MP камера",
             price=180000.0,
             quantity=5)]
    assert class_category.category_count == 1
    assert class_category.products_count == 1

def test_category_len(class_category):
    assert len(class_category) == 1


def test_get_name(class_category):
    assert class_category.get_name() == 'Смартфоны'


def test_get_description(class_category):
    assert class_category.get_description() == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'


def test_get_products(class_category):
    assert class_category.get_products() == [
        dict(name="Samsung Galaxy C23 Ultra",
             description="256GB, Серый цвет, 200MP камера",
             price=180000.0,
             quantity=5)]


@pytest.fixture
def class_product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)


def test_product_init(class_product):
    assert class_product.name == 'Samsung Galaxy C23 Ultra'
    assert class_product.description == '256GB, Серый цвет, 200MP камера'
    assert class_product.price == 180000.0
    assert class_product.quantity == 5

def test_category_len(class_product):
    assert len(class_product) == 5

def test_product_name(class_product):
    assert class_product.get_product_name() == 'Samsung Galaxy C23 Ultra'


def test_product_description(class_product):
    assert class_product.get_product_description() == '256GB, Серый цвет, 200MP камера'


def test_product_price(class_product):
    assert class_product.price == 180000.0


def test_product_quantity(class_product):
    assert class_product.get_product_quantity() == 5


@pytest.fixture
def class_smartphone():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Серебристый", 32500.0, 2, "10M fps", "Note 11", "1024GB", "Серебристый")


@pytest.fixture
def class_grass():
    return Garden_grass("Овсяница красная", "Овсяница красная (Festuca rubra L.) - корневищный и рыхлокустовой низовой многолетний злак, вид травянистых растений семейства злаковых высотой до 60см",
                        500, 1700, "Россия", "1 мес.","Красноватый")

def test_add_method(class_smartphone, class_grass):
    """ Тест метода сложения разных классов объектов"""
    with pytest.raises(TypeError):
        class_smartphone + class_grass