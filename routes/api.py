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

    # client IP detect (pehle)
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)

    if ip_address and "," in ip_address:
        ip_address = ip_address.split(",")[0].strip()

    token = data.get("token")

    if not token:
        return jsonify({"error": "Captcha token missing"}), 400

    # postman testing bypass
    if token != "test":
        if not verify_turnstile(token, ip_address):
            return jsonify({"error": "Turnstile verification failed"}), 403

    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    admin_id = 222333
    country = "Unknown"

    try:
        res = requests.get(
            f"http://ip-api.com/json/{ip_address}",
            timeout=2
        ).json()
        country = res.get("country", "Unknown")
    except Exception:
        pass

    contact = Contact(
        FullName=data['FullName'].strip(),
        Email=data['Email'].strip().lower(),
        Message=data['Message'].strip(),
        admin_id=admin_id,
        ip_address=ip_address,
        country=country
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
