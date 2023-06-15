from ..model.order import orders


def create_order(product_id, quantity):
    new_order = {
        "id": len(orders) + 1,
        "product_id": product_id,
        "quantity": quantity,
        "status": "pending",
        "shipping_code": ""
    }

    orders.append(new_order)

    return new_order
