from models.user_model import db, User

class UserService:
    def __init__(self):
        pass
        
    def add_user(self, email, name):
        """
        Add a new user to the database
        """
        user = User(email=email, name=name)
        db.session.add(user)
        db.session.commit()
        return user
    