from ..repository.create_order import create_order
from ..repository.get_product import get_product


def create_order_service(product_id, quantity):
    product = get_product(product_id)
    if product is None:
        return {
                   "error": "product id not found"
               }, 404

    return create_order(product_id, quantity)
