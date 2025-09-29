
from datetime import datetime, timezone
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
    raw_response = db.Column(db.Text)  # STORE THE COMPLETE LLM RESPONSE
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'<SupplierResponse {self.id}: {self.supplier_name}>'