from flask import Blueprint , request ,jsonify
from app.email_utils import send_email

email_bp = Blueprint('email', __name__)
@email_bp.route('/send-email', methods=['POST'])
def send_email_route():
    data = request.get_json()
    to_email = data.get('to_email')
    subject = data.get('subject')
    message = data.get('message')

    if not to_email or not subject or not message:
        return jsonify({"error": "Missing required fields"}), 400

    success = send_email(to_email, subject, message)
    if success:
        return jsonify({"message": "Email sent successfully!"}), 200
    else:
        return jsonify({"message": "Failed to send email."}), 500