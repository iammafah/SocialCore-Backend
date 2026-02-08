from .db import db

class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)

    FullName = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Message = db.Column(db.Text, nullable=False)

    admin_id = db.Column(db.Integer, nullable=True)
    # default=None unnecessary hai

    ip_address = db.Column(db.String(45), nullable=True)

    country = db.Column(db.String(80), nullable=True, default="Unknown")

    status = db.Column(db.String(20), nullable=False, default="new")

    priority = db.Column(db.String(20), nullable=False, default="normal")

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.now()
    )
