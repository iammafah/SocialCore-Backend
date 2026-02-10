import csv  # csv generate karne ke liye
import io  # memory file buffer
from flask import Blueprint, Response, g  # flask response tools

from database.models import Contact  # Contact model
from utils.admin_guard import admin_required  # admin security

csv_bp = Blueprint("csv_bp", __name__)  # new blueprint create


@csv_bp.route("/api/admin/contacts/download", methods=["GET"])  # download route
@admin_required  # admin access only
def download_contacts_csv():
    admin_id = g.admin_id  # logged-in admin id

    contacts = Contact.query.filter_by(admin_id=admin_id).all()
    # admin ke contacts DB se fetch

    output = io.StringIO()
    # memory me file create

    writer = csv.writer(output)
    # csv writer object

    writer.writerow([
        "ID",
        "FullName",
        "Email",
        "Message",
        "IP Address",
        "Country",
        "Status",
        "Priority",
        "Created At"
    ])
    # header row

    for c in contacts:
        writer.writerow([
            c.id,
            c.FullName,
            c.Email,
            c.Message,
            c.ip_address,
            c.country,
            c.status,
            c.priority,
            c.created_at
        ])
        # DB data → CSV rows

    output.seek(0)
    # pointer reset

    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=iammafah-contacts.csv"}
    )
    
