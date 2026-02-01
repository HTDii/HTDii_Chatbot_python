from flask import Blueprint
from controllers.chat_controller import chat_api

chat_bp = Blueprint("chat", __name__)

chat_bp.route("/api/chat", methods=["POST"])(chat_api)