import pytest


from src.Product_OOP import Category, Product



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


def test_category_count(category_smartphones: Category) -> None:
    assert Category.category_count == 3


def test_add_product_to_category(category_smartphones: Category) -> None:
    new_product = Product("Xiaomi Mi 10", "128GB, черный", 30000.0, 10)
    category_smartphones.add_product(new_product)
    assert len(category_smartphones.products) == 4


def test_invalid_category_product_count() -> None:
    """Проверяет, что добавление не Product приводит к ValueError."""
    category = Category("Тестовая категория", "Описание тестовой категории", [])

    # Пробуем вызвать метод добавления и перехватываем исключение
    raised_exception = False
    try:
        category.add_product(None)  # Передаем None вместо продукта
    except ValueError as e:
        raised_exception = True
        assert str(e) == "Требуется объект класса Product"

    assert raised_exception, "Ожидалось, что возникнет ValueError"


def test_category_product_list(category_smartphones: Category) -> None:
    expected_list = [
        "Samsung Galaxy S23 Ultra, 180000.00 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.00 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000.00 руб. Остаток: 14 шт.",
    ]
    assert category_smartphones.product_list == expected_list
