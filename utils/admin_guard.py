from functools import wraps
from flask import request, jsonify, g

VALID_ADMINS = [222333]

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        admin_id = None

        # POST JSON support
        if request.method == "POST":
            data = request.get_json(silent=True)
            if data:
                admin_id = data.get("admin_id")

        # GET query param support
        if not admin_id:
            admin_id = request.args.get("admin_id", type=int)

        if not admin_id:
            return jsonify({"error": "admin_id required"}), 400

        if admin_id not in VALID_ADMINS:
            return jsonify({"error": "Invalid admin_id"}), 403

        g.admin_id = admin_id
        return f(*args, **kwargs)

    return wrapper
