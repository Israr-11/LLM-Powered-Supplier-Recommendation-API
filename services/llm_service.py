import os
import json
import requests
from typing import Dict, Any, Optional
import openai
from configuration.config import Config
from utils.schema_validation import SupplierResponseSchema

class LLMService:
    def __init__(self, config=None):
        self.config = config or Config()
        self.provider = self.config.LLM_PROVIDER
        
        if self.provider == 'openai':
            openai.api_key = self.config.OPENAI_API_KEY
        elif self.provider == 'huggingface':
            self.hf_api_key = self.config.HUGGINGFACE_API_KEY
            self.hf_model = self.config.HUGGINGFACE_MODEL
    
    def generate_prompt(self, query: str) -> str:
        """Generate a prompt for the LLM to get structured supplier information."""
        return f"""
        You are a helpful AI assistant that helps businesses find the best suppliers for their needs.
        Based on the following query, provide details about the most suitable supplier.
        
        Query: {query}
        
        Please provide your response in the following JSON format:
        {{
            "supplier_name": "The name of the recommended supplier",
            "rating": A rating from 0 to 5 (can be decimal),
            "delivery_time_days": Estimated delivery time in days (integer),
            "price_estimate": Estimated price in USD (number)
        }}
        
        Only respond with the JSON, no other text.
        """
    
    async def get_supplier_recommendation(self, query: str) -> Optional[SupplierResponseSchema]:
        """Get supplier recommendation from the LLM based on the query."""
        try:
            prompt = self.generate_prompt(query)
            
            if self.provider == 'openai':
                response = await self._call_openai(prompt)
            elif self.provider == 'huggingface':
                response = await self._call_huggingface(prompt)
            else:
                raise ValueError(f"Unsupported LLM provider: {self.provider}")
            
            # Parse and validate the response
            try:
                response_dict = json.loads(response)
                validated_response = SupplierResponseSchema(**response_dict)
                return validated_response
            except json.JSONDecodeError:
                # Handle case where LLM didn't return valid JSON
                print(f"LLM didn't return valid JSON: {response}")
                return None
            except Exception as e:
                # Handle validation errors
                print(f"Validation error: {e}")
                return None
                
        except Exception as e:
            print(f"Error getting supplier recommendation: {e}")
            return None
    
    async def _call_openai(self, prompt: str) -> str:
        """Call OpenAI API with the given prompt."""
        response = await openai.chat.completions.create(
            model=self.config.OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides supplier recommendations in JSON format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    
    async def _call_huggingface(self, prompt: str) -> str:
        """Call Hugging Face API with the given prompt."""
        API_URL = f"https://api-inference.huggingface.co/models/{self.hf_model}"
        headers = {"Authorization": f"Bearer {self.hf_api_key}"}
        
        payload = {"inputs": prompt, "parameters": {"return_full_text": False}}
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0]["generated_text"]
        
        # Handle errors
        response.raise_for_status()
        return ""