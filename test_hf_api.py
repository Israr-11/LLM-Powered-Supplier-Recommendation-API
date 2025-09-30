import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_huggingface_api():
    api_key = os.getenv('HUGGINGFACE_API_KEY')
    model = os.getenv('HUGGINGFACE_MODEL', 'gpt2')
    
    print(f"Testing connection to Hugging Face API with model: {model}")
    
    api_url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    payload = {
        "inputs": "What is the capital of France?"
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        
        if response.status_code == 200:
            print("Connection successful!")
        else:
            print(f"Connection failed with status code {response.status_code}")
    except Exception as e:
        print(f"Error connecting to API: {e}")

if __name__ == "__main__":
    test_huggingface_api()