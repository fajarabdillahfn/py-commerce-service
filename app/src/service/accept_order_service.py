import random
import string

from ..repository.get_order import get_order_by_id
from ..repository.update_order import update_order_accept


def accept_order(order_id):
    order = get_order_by_id(order_id)

    if order is None:
        return {
                   "error": "order id not found"
               }, 404

    shipping_code = ''.join(random.choice(string.ascii_letters) for i in range(10))

    return update_order_accept(order, "accepted", shipping_code)
