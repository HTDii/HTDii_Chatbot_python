from openai import OpenAI

MAX_AI_TURNS = 10


class saleAIService:

    def __init__(self, context_service):
        self.context_service = context_service

    def handle_ai_reply(
        self,
        session_id: str,
        user_message: str,
        language: str | None
    ) -> dict:

        lang = language if language in ("VI", "EN", "JP") else "VI"

        # ===== GET CONTEXT =====
        context = self.context_service.get_context(session_id)

        if not context:
            print("❌ [AI] FALLBACK: context = None")
            return {
                "reply": self._fallback_message(lang)
            }

        # ===== CHECK TURN LIMIT =====
        turns = context.get("ai_count", 0)
        if turns >= MAX_AI_TURNS:
            print("⚠️ [AI] MAX_AI_TURNS reached:", turns)
            return {
                "reply": self._contact_admin_message(lang)
            }

        sale_category = context.get("sale_category")
        platform = context.get("platform")

        if not sale_category or not platform:
            print(
                "❌ [AI] FALLBACK: missing data | "
                f"sale_category={sale_category}, platform={platform}"
            )
            return {
                "reply": self._fallback_message(lang)
            }

        # ===== BUILD PROMPT =====
        system_prompt = self._build_system_prompt(lang)
        user_prompt = self._build_user_prompt(
            lang,
            sale_category,
            platform,
            user_message
        )

        client = OpenAI()

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.6,
                max_tokens=300
            )

            reply = response.choices[0].message.content.strip()

        except Exception as e:
            # ✅ LOG DUY NHẤT Ở ĐÂY
            print("💥 [AI] OpenAI ERROR:", repr(e))
            return {
                "reply": self._fallback_message(lang)
            }

        self.context_service.increase_ai_count(session_id)

        return {
            "reply": reply
        }

    # ===== PROMPTS GIỮ NGUYÊN =====

    def _build_system_prompt(self, lang: str) -> str:
        if lang == "EN":
            return (
                "You are a professional digital marketing consultant. "
                "Provide strategic, ethical, and platform-compliant advice. "
                "Avoid illegal, manipulative, or policy-violating tactics. "
                "Keep responses concise and actionable."
            )

        if lang == "JP":
            return (
                "あなたはプロフェッショナルなデジタルマーケティングコンサルタントです。"
                "各SNSの規約を遵守し、倫理的かつ実用的なアドバイスのみを提供してください。"
                "違反行為や不正手法には言及しないでください。"
            )

        return (
            "Bạn là chuyên gia tư vấn tiếp thị số chuyên nghiệp. "
            "Chỉ đưa ra giải pháp minh bạch, tuân thủ chính sách nền tảng "
            "và tránh mọi hành vi vi phạm hoặc thao túng."
        )

    def _build_user_prompt(
        self,
        lang: str,
        sale_category: str,
        platform: str,
        user_message: str
    ) -> str:

        return {
            "VI": f"""
Ngữ cảnh:
- Loại tư vấn: {sale_category}
- Nền tảng: {platform}

Câu hỏi của khách hàng:
"{user_message}"
""",
            "EN": f"""
Context:
- Consultation type: {sale_category}
- Platform: {platform}

Client question:
"{user_message}"
""",
            "JP": f"""
文脈:
- 相談内容: {sale_category}
- プラットフォーム: {platform}

ユーザーの質問:
「{user_message}」
"""
        }.get(lang)

    def _contact_admin_message(self, lang: str) -> str:
        if lang == "EN":
            return "📩 Please contact our support team for further assistance."
        if lang == "JP":
            return "📩 詳細については、サポートチームまでお問い合わせください。"
        return "📩 Vui lòng liên hệ đội ngũ hỗ trợ."

    def _fallback_message(self, lang: str) -> str:
        if lang == "EN":
            return (
                "⚠️ Our automated system is currently not fully optimized.\n"
                "You can directly experience the available SNS growth support services,\n"
                "or contact the administrator for more accurate assistance:\n"
                "📧 Email: hieutrungduongg@gmail.com\n"
                "🔵 Facebook Fanpage: https://www.facebook.com/share/17wEK1REb2/?mibextid=wwXIfr"
            )

        if lang == "JP":
            return (
                "⚠️ 現在、自動化システムはまだ完全に最適化されていません。\n"
                "既存のSNS成長支援サービスを直接ご体験いただくか、\n"
                "より正確なサポートをご希望の場合は管理者までご連絡ください。\n"
                "📧 メール: hieutrungduongg@gmail.com\n"
                "🔵 Facebookページ: https://www.facebook.com/share/17wEK1REb2"
            )

        return (
            "⚠️ Hiện tại hệ thống tự động hóa chưa được tối ưu hoàn toàn.\n"
            "Bạn có thể trực tiếp trải nghiệm các dịch vụ hỗ trợ tăng trưởng SNS có sẵn,\n"
            "hoặc liên hệ admin để được hỗ trợ chính xác hơn:\n"
            "📧 Email: hieutrungduongg@gmail.com\n"
            "🔵 Fanpage Facebook: https://www.facebook.com/share/17wEK1REb2/?mibextid=wwXIfr"
        )



