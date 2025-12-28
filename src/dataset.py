import random
import string


def generate_products(n=1000):
    """
    Gera um dataset grande de produtos simulados.

    - n: quantidade de produtos
    - IDs são aleatórios (evita árvore perfeita)
    - Dados simulam um cenário real de e-commerce
    """

    products = []
    used_ids = set()

    while len(products) < n:
        product_id = random.randint(1, n * 10)

        # garante IDs únicos
        if product_id in used_ids:
            continue
        used_ids.add(product_id)

        product = {
            "id": product_id,
            "name": generate_product_name(),
            "category": random.choice([
                "Eletrônicos",
                "Roupas",
                "Livros",
                "Casa",
                "Esporte",
                "Alimentos"
            ]),
            "price": round(random.uniform(5, 3000), 2),
            "stock": random.randint(0, 500),
            "rating": round(random.uniform(1.0, 5.0), 1)
        }

        products.append(product)

    return products


def generate_product_name():
    """
    Gera nomes de produtos aleatórios.
    """
    prefix = random.choice([
        "Ultra", "Pro", "Smart", "Eco", "Max", "Prime"
    ])
    item = random.choice([
        "Phone", "Notebook", "Camisa", "Livro", "Tênis",
        "Cadeira", "Relógio", "Fone", "Mochila"
    ])
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

    return f"{prefix} {item} {suffix}"
