class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    # Вывод информации о каждом продукте
    for product in (product1, product2, product3, product4):
        print(
            f"Наименование: {product.name}\n"
            f"Описание: {product.description}\n"
            f"Цена: {product.price}\n"
            f"Кол-во продукции: {product.quantity}\n"
        )

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    # Вывод информации о каждой категории
    for category in (category1, category2):
        print(
            f"Название категории: {category.name}\n"
            f"Описание категории: {category.description}\n"
            f"Кол-во продукции: {len(category.products)}\n"
        )

    # Вывод общего количества категорий и продуктов
    print(f"Общее кол-во категорий: {Category.category_count}")
    print(f"Общее кол-во продуктов: {Category.product_count}")
