# services/ai_context_service.py

class aiContextService:
    """
    Lưu context tạm cho SALE + AI
    In-memory, dùng cho giai đoạn đầu
    """

    def __init__(self):
        self._contexts = {}

    def init_context(self, session_id: str, language: str):
        self._contexts[session_id] = {
            "sale_category": None,
            "platform": None,
            "language": language,
            "ai_count": 0
        }

    def set_category(self, session_id: str, category: str):
        if session_id in self._contexts:
            self._contexts[session_id]["sale_category"] = category

    def set_platform(self, session_id: str, platform: str):
        if session_id in self._contexts:
            self._contexts[session_id]["platform"] = platform

    def increase_ai_count(self, session_id: str):
        if session_id in self._contexts:
            self._contexts[session_id]["ai_count"] += 1

    # ==================================================
    # 🔽 ALIAS CHO sale_ai_service (KHÔNG PHÁ CẤU TRÚC)
    # ==================================================

    def get_ai_turns(self, session_id: str) -> int:
        if session_id in self._contexts:
            return self._contexts[session_id].get("ai_count", 0)
        return 0

    def increase_ai_turns(self, session_id: str):
        self.increase_ai_count(session_id)

    # ==================================================

    def get_context(self, session_id: str):
        return self._contexts.get(session_id)

    def clear_context(self, session_id: str):
        if session_id in self._contexts:
            del self._contexts[session_id]