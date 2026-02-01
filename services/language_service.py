from messages.language_messages import (
    LANGUAGE_DEFAULT_REPLY,
    LANGUAGE_INVALID,
    SERVICE_MENU,
    BOOKING_REPLY,
    FREE_CHAT_REPLY
)

from services.sale_service import saleService


class languageService:

    def __init__(self):
        self.sale_service = saleService()

    def handle_message(self, message: str, language: str | None):

        # ===== STEP 1: CHỌN NGÔN NGỮ =====
        if message in ("JP", "EN", "VI"):
            return SERVICE_MENU.get(message)

        # ===== STEP 2: ĐÃ CÓ LANGUAGE =====
        if language in ("JP", "EN", "VI"):

            # ===== SALE FLOW (MENU / CATEGORY / PLATFORM / BACK / CTA) =====
            if message == "SALE" or message in (
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
                return self.sale_service.handle_message(message, language)


            # ===== BOOKING – dùng sau =====
            if message == "BOOKING":
                return {"reply": BOOKING_REPLY.get(language)}

            # ===== FREE CHAT – dùng sau =====
            if message == "FREE_CHAT":
                return {"reply": FREE_CHAT_REPLY.get(language)}

        # ===== FALLBACK =====
        return LANGUAGE_INVALID