import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Get individual database parameters
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5433')
    DB_NAME = os.getenv('DB_NAME', 'flask_db')
    
    # Construct the database URI from individual parameters
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI',
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS =  False

    # LLM configuration
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    LLM_PROVIDER = os.environ.get('LLM_PROVIDER', 'openai')  # 'openai' or 'huggingface'
    
    # For Hugging Face
    HUGGINGFACE_API_KEY = os.environ.get('HUGGINGFACE_API_KEY')
    HUGGINGFACE_MODEL = os.environ.get('HUGGINGFACE_MODEL', 'mistralai/Mistral-7B-Instruct-v0.2')
    
    # For OpenAI
    OPENAI_MODEL = os.environ.get('OPENAI_MODEL', 'gpt-3.5-turbo')