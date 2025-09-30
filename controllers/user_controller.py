from flask import jsonify
from services.user_service import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()
    
    def add_user(self, email, name):
        """
        Controller method to add a user
        """
        user = self.user_service.add_user(email, name)
        return jsonify({"message": f"User {user.name} added successfully", "user": user.to_dict()}), 201
    