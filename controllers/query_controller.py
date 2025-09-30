from flask import request, jsonify
from services.query_service import QueryService

class QueryController:
    def __init__(self):
        self.query_service = QueryService()
    
    def process_query(self):
        """Handle query processing request."""
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({"error": "Missing query parameter"}), 400
        
        # For simplicity, using user_id=1; in a real app, get from auth
        user_id = 1
        query_text = data['query']
        
        result = self.query_service.process_query(user_id, query_text)
        
        if result.get("success", False):
            return jsonify(result), 200
        else:
            return jsonify(result), 500
    
    def get_history(self):
        """Handle request to get query history."""
        # For simplicity, using user_id=1; in a real app, get from auth
        user_id = 1
        
        history = self.query_service.get_query_history(user_id)
        return jsonify({"history": history}), 200