from .db import db                # Import database instance
class Contact(db.Model):         # ORM model for contact messages
    __tablename__ = 'contact'    # Explicit table name
    
    id = db.Column(db.Integer, primary_key=True)         # Primary key
    FullName = db.Column(db.String(100), nullable=False) # Sender full name
    Email = db.Column(db.String(100), nullable=False)    # Sender email address
    Message = db.Column(db.Text, nullable=False)         # Message content
