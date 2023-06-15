from flask import Blueprint

from ..controller.create_order import create_order_controller
from ..controller.accept_order import accept_order_controller

blueprint = Blueprint('blueprint', __name__)

blueprint.route("/order", methods=["POST"])(create_order_controller)
blueprint.route("/order/accept", methods=["POST"])(accept_order_controller)