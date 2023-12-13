from dataclasses import dataclass


@dataclass
class Article:
    """
    an article in the farmshop
    """
    name: str
    price: float
    stock: int


if __name__ == '__main__':
    pass