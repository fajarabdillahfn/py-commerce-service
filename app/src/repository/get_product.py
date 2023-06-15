from ..model.product import products


def get_product(product_id):
    is_valid = False
    index = 0

    for i, product in enumerate(products):
        if product["product_id"] == product_id:
            is_valid = True
            index = i
            break

    if not is_valid:
        return None

    return products[index]