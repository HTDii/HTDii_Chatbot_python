from messages.sale_messages import (
    SALE_INTRO,
    SALE_MENU,
    SALE_CATEGORY_REPLY,
    SALE_PLATFORM_OPTIONS,
    SALE_PLATFORM_REPLY,   # GIỮ, KHÔNG XOÁ (DÙ KHÔNG DÙNG NỮA)
    SALE_CTA_OPTIONS,      # GIỮ, KHÔNG XOÁ
    SALE_FALLBACK
)


class saleService:

    def handle_message(self, message: str, language: str | None) -> dict:
        lang = language if language in ("VI", "EN", "JP") else "VI"

        # ===== ENTRY =====
        if message == "SALE":
            return {
                "reply": SALE_INTRO.get(lang),
                "options": SALE_MENU.get(lang)
            }

        # ===== CATEGORY =====
        if message in SALE_CATEGORY_REPLY:
            return {
                "reply": SALE_CATEGORY_REPLY[message].get(lang),
                "options": SALE_PLATFORM_OPTIONS.get(lang),
                # 👇 CHỈ TRẢ CONTEXT, KHÔNG SET
                "context": {
                    "sale_category": message
                }
            }

        # ===== PLATFORM =====
        # 👉 TẠI ĐÂY AI PHẢI XUẤT HIỆN NGAY
        if message in ("TIKTOK", "FACEBOOK", "TELEGRAM", "INSTAGRAM", "YOUTUBE"):
            return {
                # ❌ KHÔNG TRẢ reply tĩnh nữa
                # ❌ KHÔNG options
                # 👉 CHỈ TRẢ CONTEXT + CỜ BÁO GỌI AI
                "context": {
                    "platform": message
                },
                "use_ai": True
            }

        # ===== BACK =====
        if message == "BACK_TO_SALE_MENU":
            return {
                "reply": SALE_INTRO.get(lang),
                "options": SALE_MENU.get(lang)
            }

        # ===== FALLBACK =====
        return {
            "reply": SALE_FALLBACK.get(lang),
            "options": SALE_CTA_OPTIONS.get(lang)
        }