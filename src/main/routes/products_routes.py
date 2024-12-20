from flask import Blueprint, jsonify, request

from src.http_types.http_request import HttpRequest
from src.main.composer.product_creator_composer import product_creator_composer
from src.main.composer.product_finder_composer import product_finder_composer

products_routes_bp = Blueprint("products_routes", __name__)


@products_routes_bp.route("/products", methods=["POST"])
def insert_product():
    http_request = HttpRequest(body=request.json)
    usecase = product_creator_composer()
    response = usecase.create(http_request)

    return jsonify(response.body), response.status_code


@products_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name):
    http_request = HttpRequest(path_params={"product_name": product_name})
    usecase = product_finder_composer()
    response = usecase.find_by_name(http_request)

    return jsonify(response.body), response.status_code
