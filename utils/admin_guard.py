from functools import wraps
from flask import request, jsonify

VALID_ADMINS = [222333]  # temporary admin ids

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        data = request.get_json()

        admin_id = data.get("admin_id")

        if admin_id not in VALID_ADMINS:
            return jsonify({"error": "Invalid admin_id"}), 403

        return f(*args, **kwargs)

    return wrapper
