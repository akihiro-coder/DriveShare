from flask import Blueprint, jsonify, request
from driveshare.models import Route
from driveshare.services.route_service import get_all_routes


api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/routes', methods=['GET'])
def get_routes():
    routes = get_all_routes()
    return jsonify(
        {'routes': [route.model_dump() for route in routes]}
    )