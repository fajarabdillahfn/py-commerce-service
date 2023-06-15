from ..model.order import orders


def get_order_by_id(order_id):
    is_valid = False
    index = 0

    for i, order in enumerate(orders):
        if order["id"] == order_id:
            is_valid = True
            index = i
            break

    if not is_valid:
        return None

    return orders[index]