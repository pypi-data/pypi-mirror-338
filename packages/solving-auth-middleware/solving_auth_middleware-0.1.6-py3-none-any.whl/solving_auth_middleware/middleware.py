from flask import request, jsonify
from functools import wraps
from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt,
    get_jwt_identity
)

def requires_auth(required_scopes=None, required_roles=None, audit_fn=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                verify_jwt_in_request()
                jwt_data = get_jwt()
                identity = get_jwt_identity()

                token_scopes = jwt_data.get("scopes", [])
                token_roles = jwt_data.get("roles", [])

                if required_scopes:
                    for scope in required_scopes:
                        if scope not in token_scopes:
                            return jsonify({"msg": f"Missing scope: {scope}"}), 403

                if required_roles:
                    if not any(role in token_roles for role in required_roles):
                        return jsonify({"msg": "Insufficient role"}), 403

                if audit_fn:
                    audit_fn(identity, request)

            except Exception as e:
                return jsonify({"msg": "Unauthorized", "error": str(e)}), 401

            return fn(*args, **kwargs)
        return decorator
    return wrapper