from messages.sale_messages import (
    SALE_INTRO,
    SALE_MENU,
    SALE_CATEGORY_REPLY,
    SALE_PLATFORM_OPTIONS,
    SALE_PLATFORM_REPLY,
    SALE_CTA_OPTIONS,
    SALE_FALLBACK
)


class saleService:

    def handle_message(self, message: str, language: str | None) -> dict:
        lang = language if language in ("VI", "EN", "JP") else "VI"

        # ===== ENTRY =====
        if message == "SALE":
            result = {}
            result.update(SALE_INTRO.get(lang))
            result.update(SALE_MENU.get(lang))
            return result

        # ===== CATEGORY =====
        if message in SALE_CATEGORY_REPLY:
            result = {}
            result.update(SALE_CATEGORY_REPLY[message].get(lang))
            result.update(SALE_PLATFORM_OPTIONS.get(lang))
            result["context"] = {
                "sale_category": message
            }
            return result

        # ===== PLATFORM =====
        if message in ("TIKTOK", "FACEBOOK", "TELEGRAM", "INSTAGRAM", "YOUTUBE"):
            return {
                "context": {
                    "platform": message
                },
                "use_ai": True
            }

        # ===== BACK =====
        if message == "BACK_TO_SALE_MENU":
            result = {}
            result.update(SALE_INTRO.get(lang))
            result.update(SALE_MENU.get(lang))
            return result

        # ===== FALLBACK =====
        result = {}
        result.update(SALE_FALLBACK.get(lang))
        result.update(SALE_CTA_OPTIONS.get(lang))
        return result