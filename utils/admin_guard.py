from functools import wraps
from flask import request, jsonify, g

VALID_ADMINS = [222333]  # temporary admin ids

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        data = request.get_json(silent=True)

        if not data or "admin_id" not in data:
            return jsonify({"error": "admin_id required"}), 400

        admin_id = data.get("admin_id")

        if admin_id not in VALID_ADMINS:
            return jsonify({"error": "Invalid admin_id"}), 403

        g.admin_id = admin_id  # request context me store

        return f(*args, **kwargs)

    return wrapper
