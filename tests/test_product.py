import pytest

from src.Product_OOP import (  
    Category, Product)


# Фикстуры для продуктов
@pytest.fixture
def product_samsung() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_iphone() -> Product: 
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_xiaomi() -> Product:  
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def product_tv() -> Product:
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


# Фикстуры для категорий
@pytest.fixture
def category_smartphones(product_samsung: Product, product_iphone: Product, product_xiaomi: Product) -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_samsung, product_iphone, product_xiaomi],
    )


@pytest.fixture
def category_tv(product_tv: Product) -> Category:
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product_tv],
    )


def test_product_initialization(product_samsung: Product, product_iphone: Product, product_xiaomi: Product) -> None:
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8
    assert product_xiaomi.name == "Xiaomi Redmi Note 11"
    assert product_xiaomi.description == "1024GB, Синий"
    assert product_xiaomi.price == 31000.0
    assert product_xiaomi.quantity == 14


def test_category_initialization(category_smartphones: Category, category_tv: Category) -> None:
    assert category_smartphones.name == "Смартфоны"
    assert (
        category_smartphones.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_smartphones.products) == 3
    assert category_tv.name == "Телевизоры"
    assert (
        category_tv.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category_tv.products) == 1


def test_category_count() -> None:
    Category.category_count = 0
    Category.product_count = 0
    product1 = Product("Test Product 1", "Testing product", 100.0, 1)
    product2 = Product("Test Product 2", "Testing product", 100.0, 1)
    category = Category("Test Category", "Testing category", [product1, product2])
    assert category.category_count == 1
    assert category.product_count == 2


def test_category_product_count_with_multiple_categories() -> None:
    Category.category_count = 0
    Category.product_count = 0
    product1 = Product("Product 1", "Test product 1", 100.0, 1)
    category1 = Category("Category 1", "Test category 1", [product1])
    assert category1.category_count == 1
    assert category1.product_count == 1
