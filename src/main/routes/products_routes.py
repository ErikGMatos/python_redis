from flask import Blueprint

products_routes_bp = Blueprint("products_routes", __name__)


@products_routes_bp.route("/products", methods=["POST"])
def insert_product():
    return "POST PRODUCTS"


@products_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name):
    return product_name
