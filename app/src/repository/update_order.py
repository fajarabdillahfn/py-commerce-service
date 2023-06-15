def update_order_accept(order, status, shipping_code):
    order["status"] = status
    order["shipping_code"] = shipping_code

    return order
