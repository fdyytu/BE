from .product import Product

class DigitalProduct(Product):
    """Digital product specifics."""

    def __init__(self, name: str, price: float, download_url: str):
        super().__init__(name, price)
        self.download_url = download_url