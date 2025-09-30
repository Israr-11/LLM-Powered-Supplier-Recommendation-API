from datetime import datetime, timezone
from models.user_model import db

class Query(db.Model):
    __tablename__ = 'queries'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    query_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    # WE'LL DEFINE THE RELATIONSHIP AFTER BOTH CLASSES ARE DEFINED
    # TO AVOID THE CIRCULAR IMPORT ISSUE
    
    def __repr__(self):
        return f'<Query {self.id}: {self.query_text[:20]}...>'

# IMPORT HERE AFTER QUERY CLASS IS DEFINED
from models.supplier_response_model import SupplierResponse

# NOW DEFINING THE RELATIONSHIP
Query.response = db.relationship('SupplierResponse', backref='query', lazy=True, uselist=False)