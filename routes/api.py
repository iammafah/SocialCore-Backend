from flask import Blueprint,request,jsonify
from database.db import db
from schemas.contact_schema import ContactSchema
from database import Contact

api_bp = Blueprint('api',__name__)
schema = ContactSchema()

@api_bp.route('/api/contacts', methods=['POST'])
def create_contact():                                 # Create and store a contact message after validation
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    contact = Contact(
        FullName=data['FullName'],
        Email=data['Email'],
        Message=data['Message']
    
    )
    check = Contact.query.filter_by(Email=data['Email']).first()
    if check:
        return jsonify({'message': 'Email already exists'}), 400
    db.session.add(contact)
    db.session.commit()
    return jsonify({'message': 'Contact created successfully'}), 201

