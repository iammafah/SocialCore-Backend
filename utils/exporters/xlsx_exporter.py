from flask import Blueprint, send_file, g  # flask tools
from database.models import Contact  # Contact model
from utils.admin_guard import admin_required  # admin security

from openpyxl import Workbook  # excel workbook create
import io  # memory buffer

xlsx_bp = Blueprint("xlsx_bp", __name__)  # blueprint create


@xlsx_bp.route("/api/admin/contacts/download/xlsx", methods=["GET"])  # route
@admin_required  # admin only
def download_contacts_xlsx():
    admin_id = g.admin_id  # logged-in admin id

    contacts = Contact.query.filter_by(admin_id=admin_id).all()
    # DB se contacts fetch

    wb = Workbook()  # workbook create
    ws = wb.active  # active sheet
    ws.title = "Contacts"  # sheet name

    ws.append([
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
        ws.append([
            c.id,
            c.FullName,
            c.Email,
            c.Message,
            c.ip_address,
            c.country,
            c.status,
            c.priority,
            str(c.created_at)
        ])
        # DB rows add

    output = io.BytesIO()  # memory file
    wb.save(output)  # workbook save
    output.seek(0)  # pointer reset

    return send_file(
        output,
        as_attachment=True,
        download_name="iammafah-contacts.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
