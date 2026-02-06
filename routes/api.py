from flask import Blueprint, request, jsonify
from database.db import db
from schemas.contact_schema import ContactSchema
from database.models import Contact   # ✅ FIXED IMPORT

api_bp = Blueprint('api', __name__)
schema = ContactSchema()

@api_bp.route('/api/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    email = data['Email'].strip().lower()

    check = Contact.query.filter_by(Email=email).first()
    if check:
        return jsonify({'message': 'Email already exists'}), 400

    contact = Contact(
        FullName=data['FullName'].strip(),
        Email=email,
        Message=data['Message'].strip()
    )

    db.session.add(contact)
    db.session.commit()

    return jsonify({'message': 'Contact created successfully'}), 201
