class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для получения цены продукта."""
        return self.__price

    @price.setter
    def price(self, value: float):
        """Сеттер для установки цены продукта с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_info: dict):
        """Класс-метод для создания нового продукта из словаря."""
        return cls(
            name=product_info['name'],
            description=product_info['description'],
            price=product_info['price'],
            quantity=product_info['quantity']
        )

    def __str__(self):
        return (
            f"Наименование: {self.name}\n"
            f"Описание: {self.description}\n"
            f"Цена: {self.price:.2f} руб.\n"
            f"Кол-во продукции: {self.quantity}\n"
        )


class Category:
    category_count: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут
        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise ValueError("Требуется объект класса Product")

    @property
    def products(self):
        return self.__products

    @property
    def product_list(self):
        return [
            f"{product.name}, {product.price:.2f} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        ]

    def __str__(self):
        return (
            f"Название категории: {self.name}\n"
            f"Описание категории: {self.description}\n"
            f"Кол-во продукции: {len(self.__products)}\n"
        )


if __name__ == "__main__":
    product_info1 = {
        'name': "Samsung Galaxy S23 Ultra",
        'description': "256GB, Серый цвет, 200MP камера",
        'price': 180000.0,
        'quantity': 5
    }

    product_info2 = {
        'name': "Iphone 15",
        'description': "512GB, Gray space",
        'price': 210000.0,
        'quantity': 8
    }

    product_info3 = {
        'name': "Xiaomi Redmi Note 11",
        'description': "1024GB, Синий",
        'price': 31000.0,
        'quantity': 14
    }

    product_info4 = {
        'name': '55" QLED 4K',
        'description': "Фоновая подсветка",
        'price': 123000.0,
        'quantity': 7
    }

    # Использование метода new_product для создания объектов
    product1 = Product.new_product(product_info1)
    product2 = Product.new_product(product_info2)
    product3 = Product.new_product(product_info3)
    product4 = Product.new_product(product_info4)

    # Вывод информации о каждом продукте
    for product in (product1, product2, product3, product4):
        print(product)

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
        print(f"{category}\n")

        # Вывод списка товаров данной категории
        print("Список товаров в категории:")
        for product_info in category.product_list:
            print(f"{product_info}\n")

    # Вывод общего количества категорий
    print(f"\nОбщее кол-во категорий: {Category.category_count}")
