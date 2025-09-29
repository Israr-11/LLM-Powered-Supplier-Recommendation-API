from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Query(db.Model):
    __tablename__ = 'queries'
    
    id = db.Column(db.Integer, primary_key=True)
    query_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Relationship with responses
    response = db.relationship('SupplierResponse', backref='query', lazy=True, uselist=False)
    
    def __repr__(self):
        return f'<Query {self.id}: {self.query_text[:20]}...>'
