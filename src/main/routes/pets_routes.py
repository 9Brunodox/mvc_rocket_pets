from flask import Blueprint, jsonify

pet_route_bp = Blueprint('pet_route', __name__)

@pet_route_bp.route('/pets', methods=['GET'])
def list_pets():
    return jsonify({"message": "List of pets"}), 200