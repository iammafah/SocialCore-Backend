import requests   # HTTP API call ke liye
from flask import Blueprint, request, jsonify   # Flask utilities
from database.db import db                      # DB instance
from schemas.contact_schema import ContactSchema
from database.models import Contact
from utils.admin_guard import admin_required
api_bp = Blueprint('api', __name__)
schema = ContactSchema()

@api_bp.route('/api/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()  # JSON body read

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    errors = schema.validate(data)  # validation
    if errors:
        return jsonify(errors), 400

    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    # client IP detect
    admin_id = 222333

    country = "Unknown"  # default value

    try:
        res = requests.get(f"http://ip-api.com/json/{ip_address}").json()
        country = res.get("country", "Unknown")  
        # API se country nikaal rahe hain
    except:
        pass  # agar API fail ho jaye

    contact = Contact(
        FullName=data['FullName'].strip(),  # name clean
        Email=data['Email'].strip().lower(),  # email normalize
        Message=data['Message'].strip(),  # message clean
        admin_id=admin_id,  # temporary admin
        ip_address=ip_address,  # IP save
        country=country  # country save
    )

    db.session.add(contact)  # add to DB
    db.session.commit()  # save

    return jsonify({'message': 'Contact created successfully'}), 201


@api_bp.route("/api/admin/contacts", methods=["POST"])
@admin_required
def get_admin_contacts():
    data = request.get_json()

    admin_id = data["admin_id"]

    contacts = Contact.query.filter_by(admin_id=admin_id).all()

    return jsonify(ContactSchema(many=True).dump(contacts))
