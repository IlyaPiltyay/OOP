from typing import Any, Dict, List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут для хранения цены
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для получения цены продукта."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для установки цены продукта с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value  # Сохраняем новое значение

    @classmethod
    def new_product(cls, product_info: Dict[str, Any]) -> "Product":
        """Класс-метод для создания нового продукта из словаря."""
        return cls(
            name=product_info["name"],
            description=product_info["description"],
            price=product_info["price"],
            quantity=product_info["quantity"],
        )


class Category:
    category_count: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self._products = products  # Приватный атрибут для хранения списка продуктов
        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self._products.append(product)
        else:
            raise ValueError("Требуется объект класса Product")

    @property
    def products(self) -> List[Product]:
        return self._products

    @property
    def product_list(self) -> List[str]:
        return [
            f"{product.name}, {product.price:.2f} руб. Остаток: {product.quantity} шт." for product in self._products
        ]


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_list)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
