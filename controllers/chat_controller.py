from flask import request, jsonify
from services.language_service import languageService
from services.ai_context_service import aiContextService
from services.sale_ai_service import saleAIService

language_service = languageService()
context_service = aiContextService()
ai_service = saleAIService(context_service)


def chat_api():
    data = request.json or {}

    message = data.get("message", "")
    language = data.get("language")

    # ==============================
    # SESSION (DEV: IP)
    # ==============================
    session_id = request.remote_addr

    # ==============================
    # INIT CONTEXT KHI CHỌN NGÔN NGỮ
    # ==============================
    if message in ("VI", "EN", "JP"):
        context_service.init_context(session_id, message)

    # ==============================
    # GỌI LOGIC CHÍNH
    # ==============================
    result = language_service.handle_message(message, language)

    # ==============================
    # GHI CONTEXT NẾU CÓ
    # ==============================
    if isinstance(result, dict) and "context" in result:
        ctx = result["context"]

        if "sale_category" in ctx:
            context_service.set_category(session_id, ctx["sale_category"])

        if "platform" in ctx:
            context_service.set_platform(session_id, ctx["platform"])

        # ❌ KHÔNG TRẢ CONTEXT VỀ FRONTEND
        result.pop("context")

    # ==============================
    # CHECK & CALL AI
    # ==============================
    current_context = context_service.get_context(session_id)

    if (
        current_context
        and current_context.get("sale_category")
        and current_context.get("platform")
        and isinstance(result, dict)
    ):
        # Nếu là bước chọn platform (use_ai=True)
        # HOẶC là chat tự do sau khi đã có đủ context
        if result.get("use_ai") is True or message not in (
            "SNS_PERSONAL",
            "BRAND_BUILDING",
            "KOL_SUPPORT",
            "GENERAL_GOAL",
            "TIKTOK",
            "FACEBOOK",
            "TELEGRAM",
            "INSTAGRAM",
            "YOUTUBE",
            "REQUEST_CONSULT",
            "BACK_TO_SALE_MENU"
        ):
            print(
                "🤖 [AI CALL]",
                "| language =", current_context.get("language"),
                "| category =", current_context.get("sale_category"),
                "| platform =", current_context.get("platform"),
            )

            ai_result = ai_service.handle_ai_reply(
                session_id=session_id,
                user_message=message,
                language=language
            )
            return jsonify(ai_result)

    # ==============================
    # TRẢ RESPONSE THƯỜNG
    # ==============================
    return jsonify(result)