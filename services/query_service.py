from typing import List, Dict, Optional
from models.user_model import db
from models.query_model import Query
from models.supplier_response_model import SupplierResponse  # Make sure this import is correct
from services.llm_service import LLMService
from utils.schema_validation import SupplierResponseSchema

class QueryService:
    def __init__(self):
        self.llm_service = LLMService()
    
    def process_query(self, user_id: int, query_text: str) -> Dict:
        """Process a user query and return supplier recommendations."""
        try:
            # Create and save query record
            query = Query(user_id=user_id, query_text=query_text)
            db.session.add(query)
            db.session.flush()  # Get the query ID without committing
            
            # Get recommendation from LLM
            recommendation = self.llm_service.get_supplier_recommendation(query_text)
            
            if recommendation:
                # Create response record
                response = SupplierResponse(
                    query_id=query.id,
                    supplier_name=recommendation.supplier_name,
                    rating=recommendation.rating,
                    delivery_time_days=recommendation.delivery_time_days,
                    price_estimate=recommendation.price_estimate,
                    raw_response=str(recommendation.model_dump())
                )
                db.session.add(response)
                db.session.commit()
                
                return {
                    "success": True,
                    "query_id": query.id,
                    "recommendation": recommendation.model_dump()
                }
            else:
                # Save the query even if recommendation failed
                db.session.commit()
                return {
                    "success": False,
                    "query_id": query.id,
                    "error": "Failed to generate supplier recommendation"
                }
                
        except Exception as e:
            db.session.rollback()
            return {"success": False, "error": str(e)}
    
    def get_query_history(self, user_id: int) -> List[Dict]:
        """Get query history for a user."""
        queries = Query.query.filter_by(user_id=user_id).order_by(Query.created_at.desc()).all()
        
        result = []
        for query in queries:
            query_data = {
                "id": query.id,
                "query_text": query.query_text,
                "created_at": query.created_at.isoformat()
            }
            
            if query.response:
                query_data["response"] = {
                    "supplier_name": query.response.supplier_name,
                    "rating": query.response.rating,
                    "delivery_time_days": query.response.delivery_time_days,
                    "price_estimate": query.response.price_estimate,
                }
            else:
                query_data["response"] = None
                
            result.append(query_data)
            
        return result