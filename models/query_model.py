from datetime import datetime
from models.user_model import db

class Query(db.Model):
    __tablename__ = 'queries'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    query_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship with responses
    response = db.relationship('SupplierResponse', backref='query', lazy=True, uselist=False)
    
    def __repr__(self):
        return f'<Query {self.id}: {self.query_text[:20]}...>'
