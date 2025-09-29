
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SupplierResponse(db.Model):
    __tablename__ = 'supplier_responses'
    
    id = db.Column(db.Integer, primary_key=True)
    query_id = db.Column(db.Integer, db.ForeignKey('queries.id'), nullable=False)
    supplier_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float)
    delivery_time_days = db.Column(db.Integer)
    price_estimate = db.Column(db.Float)
    raw_response = db.Column(db.Text)  # Store the complete LLM response
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<SupplierResponse {self.id}: {self.supplier_name}>'