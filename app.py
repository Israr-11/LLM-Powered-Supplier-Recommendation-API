from flask import Flask
from configuration.config import Config
from models.user_model import db
from routes.query_routes import query_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(query_bp)
    
    @app.route('/')
    def home():
        return {"message": "LLM Supplier Recommendation API is running!"}
    
    return app

if __name__ == '__main__':
    app = create_app()
    # Create tables on startup
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)