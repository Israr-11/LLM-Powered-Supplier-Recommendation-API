from flask import Blueprint, request
from controllers.user_controller import UserController

user_bp = Blueprint('user', __name__)
user_controller = UserController()

@user_bp.route('/add_user', methods=['POST'])
def add_user():
    email = request.json.get('email')
    name = request.json.get('name')
    return user_controller.add_user(email, name)
