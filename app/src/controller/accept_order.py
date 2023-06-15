from flask import request
from ..service.accept_order_service import accept_order


def accept_order_controller():
    request_data = request.get_json()

    if "order_id" not in request_data:
        return {
                   "error": "order_id is required"
               }, 400

    order_id = request_data["order_id"]

    return accept_order(order_id)