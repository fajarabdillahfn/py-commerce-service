from flask import request
from ..service.create_order_service import create_order_service


def create_order_controller():
    request_data = request.get_json()

    if "product_id" not in request_data:
        return {
                   "error": "product_id is required"
               }, 400

    if "quantity" not in request_data:
        return {
                   "error": "quantity is required"
               }, 400

    product_id = request_data["product_id"]
    quantity = request_data["quantity"]

    return create_order_service(product_id, quantity)
