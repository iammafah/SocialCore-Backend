import requests
from flask import Blueprint, request, jsonify,g
from database.db import db
from schemas.contact_schema import ContactSchema
from database.models import Contact
from utils.admin_guard import admin_required
from utils.turnstile import verify_turnstile


api_bp = Blueprint('api', __name__)
schema = ContactSchema()


@api_bp.route('/api/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)

    token = data.get("token")

    if not token:
        return jsonify({"error": "Captcha token missing"}), 400

    if not verify_turnstile(token, ip_address):
        return jsonify({"error": "Turnstile verification failed"}), 403

    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    contact = Contact(
        FullName=data['FullName'].strip(),
        Email=data['Email'].strip().lower(),
        Message=data['Message'].strip(),
        admin_id=222333,
        ip_address=ip_address
    )

    db.session.add(contact)
    db.session.commit()

    return jsonify({'message': 'Contact created successfully'}), 201

@api_bp.route("/api/admin/contacts", methods=["POST"])
@admin_required
def get_admin_contacts():
    admin_id = g.admin_id

    contacts = Contact.query.filter_by(admin_id=admin_id).all()

    return jsonify(ContactSchema(many=True).dump(contacts))
