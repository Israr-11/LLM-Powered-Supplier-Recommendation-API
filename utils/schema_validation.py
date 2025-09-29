from typing import Optional
from pydantic import BaseModel, Field, field_validator

class QueryRequest(BaseModel):
    query: str = Field(..., description="User query for supplier recommendations")
    
    @field_validator('query')
    def query_not_empty(cls, v):
        if not v.strip():
            raise ValueError("Query cannot be empty")
        return v

class SupplierResponseSchema(BaseModel):
    supplier_name: str = Field(..., description="Name of the recommended supplier")
    rating: Optional[float] = Field(None, description="Supplier rating out of 5.0")
    delivery_time_days: Optional[int] = Field(None, description="Estimated delivery time in days")
    price_estimate: Optional[float] = Field(None, description="Estimated price for the order")
    
    @field_validator('rating')
    def validate_rating(cls, v):
        if v is not None and (v < 0 or v > 5):
            raise ValueError("Rating must be between 0 and 5")
        return v
    
    @field_validator('delivery_time_days')
    def validate_delivery_time(cls, v):
        if v is not None and v < 0:
            raise ValueError("Delivery time cannot be negative")
        return v
    
    @field_validator('price_estimate')
    def validate_price(cls, v):
        if v is not None and v < 0:
            raise ValueError("Price estimate cannot be negative")
        return v