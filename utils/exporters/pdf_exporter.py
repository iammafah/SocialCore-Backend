from flask import Blueprint, send_file, g  # flask tools
from database.models import Contact  # Contact model
from utils.admin_guard import admin_required  # admin security

from reportlab.lib.pagesizes import letter  # page size
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer  # pdf elements
from reportlab.lib.styles import getSampleStyleSheet  # text style

import io  # memory buffer

pdf_bp = Blueprint("pdf_bp", __name__)  # blueprint


@pdf_bp.route("/api/admin/contacts/download/pdf", methods=["GET"])  # route
@admin_required  # admin only
def download_contacts_pdf():
    admin_id = g.admin_id  # admin id

    contacts = Contact.query.filter_by(admin_id=admin_id).all()
    # DB fetch

    output = io.BytesIO()  # memory file

    doc = SimpleDocTemplate(output, pagesize=letter)
    # pdf document create

    styles = getSampleStyleSheet()  # default styles
    elements = []  # pdf content list

    elements.append(Paragraph("Contacts Report", styles["Title"]))
    # title

    elements.append(Spacer(1, 12))
    # spacing

    for c in contacts:
        text = f"{c.FullName} | {c.Email} | {c.country} | {c.status}"
        elements.append(Paragraph(text, styles["Normal"]))
        elements.append(Spacer(1, 8))
        # contact line

    doc.build(elements)  # pdf build

    output.seek(0)  # pointer reset

    return send_file(
        output,
        as_attachment=True,
        download_name="iammafah-contacts.pdf",
        mimetype="application/pdf"
    )
