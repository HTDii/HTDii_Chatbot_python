# from openai import OpenAI

# MAX_AI_TURNS = 10


# class saleAIService:

#     def __init__(self, context_service):
#         self.context_service = context_service

#     def handle_ai_reply(
#         self,
#         session_id: str,
#         user_message: str,
#         language: str | None
#     ) -> dict:

#         lang = language if language in ("VI", "EN", "JP") else "VI"

#         # ===== GET CONTEXT =====
#         context = self.context_service.get_context(session_id)

#         if not context:
#             print("❌ [AI] FALLBACK: context = None")
#             return {
#                 "reply": self._fallback_message(lang)
#             }

#         # ===== CHECK TURN LIMIT =====
#         turns = context.get("ai_count", 0)
#         if turns >= MAX_AI_TURNS:
#             print("⚠️ [AI] MAX_AI_TURNS reached:", turns)
#             return {
#                 "reply": self._contact_admin_message(lang)
#             }

#         sale_category = context.get("sale_category")
#         platform = context.get("platform")

#         if not sale_category or not platform:
#             print(
#                 "❌ [AI] FALLBACK: missing data | "
#                 f"sale_category={sale_category}, platform={platform}"
#             )
#             return {
#                 "reply": self._fallback_message(lang)
#             }

#         # ===== BUILD PROMPT =====
#         system_prompt = self._build_system_prompt(lang)
#         user_prompt = self._build_user_prompt(
#             lang,
#             sale_category,
#             platform,
#             user_message
#         )

#         client = OpenAI()

#         try:
#             response = client.chat.completions.create(
#                 model="gpt-4o-mini",
#                 messages=[
#                     {"role": "system", "content": system_prompt},
#                     {"role": "user", "content": user_prompt}
#                 ],
#                 temperature=0.6,
#                 max_tokens=300
#             )

#             reply = response.choices[0].message.content.strip()

#         except Exception as e:
#             # ✅ LOG DUY NHẤT Ở ĐÂY
#             print("💥 [AI] OpenAI ERROR:", repr(e))
#             return {
#                 "reply": self._fallback_message(lang)
#             }

#         self.context_service.increase_ai_count(session_id)

#         return {
#             "reply": reply
#         }

#     # ===== PROMPTS GIỮ NGUYÊN =====

#     def _build_system_prompt(self, lang: str) -> str:
#         if lang == "EN":
#             return (
#                 "You are a professional digital marketing consultant. "
#                 "Provide strategic, ethical, and platform-compliant advice. "
#                 "Avoid illegal, manipulative, or policy-violating tactics. "
#                 "Keep responses concise and actionable."
#             )

#         if lang == "JP":
#             return (
#                 "あなたはプロフェッショナルなデジタルマーケティングコンサルタントです。"
#                 "各SNSの規約を遵守し、倫理的かつ実用的なアドバイスのみを提供してください。"
#                 "違反行為や不正手法には言及しないでください。"
#             )

#         return (
#             "Bạn là chuyên gia tư vấn tiếp thị số chuyên nghiệp. "
#             "Chỉ đưa ra giải pháp minh bạch, tuân thủ chính sách nền tảng "
#             "và tránh mọi hành vi vi phạm hoặc thao túng."
#         )

#     def _build_user_prompt(
#         self,
#         lang: str,
#         sale_category: str,
#         platform: str,
#         user_message: str
#     ) -> str:

#         return {
#             "VI": f"""
# Ngữ cảnh:
# - Loại tư vấn: {sale_category}
# - Nền tảng: {platform}

# Câu hỏi của khách hàng:
# "{user_message}"
# """,
#             "EN": f"""
# Context:
# - Consultation type: {sale_category}
# - Platform: {platform}

# Client question:
# "{user_message}"
# """,
#             "JP": f"""
# 文脈:
# - 相談内容: {sale_category}
# - プラットフォーム: {platform}

# ユーザーの質問:
# 「{user_message}」
# """
#         }.get(lang)

#     def _contact_admin_message(self, lang: str) -> str:
#         if lang == "EN":
#             return "📩 Please contact our support team for further assistance."
#         if lang == "JP":
#             return "📩 詳細については、サポートチームまでお問い合わせください。"
#         return "📩 Vui lòng liên hệ đội ngũ hỗ trợ."

#     def _fallback_message(self, lang: str) -> str:
#         if lang == "EN":
#             return (
#                 "⚠️ Our automated system is currently not fully optimized.\n"
#                 "You can directly experience the available SNS growth support services,\n"
#                 "or contact the administrator for more accurate assistance:\n"
#                 "📧 Email: hieutrungduongg@gmail.com\n"
#                 "🔵 Facebook Fanpage: https://www.facebook.com/share/17wEK1REb2/?mibextid=wwXIfr"
#             )

#         if lang == "JP":
#             return (
#                 "⚠️ 現在、自動化システムはまだ完全に最適化されていません。\n"
#                 "既存のSNS成長支援サービスを直接ご体験いただくか、\n"
#                 "より正確なサポートをご希望の場合は管理者までご連絡ください。\n"
#                 "📧 メール: hieutrungduongg@gmail.com\n"
#                 "🔵 Facebookページ: https://www.facebook.com/share/17wEK1REb2"
#             )

#         return (
#             "⚠️ Hiện tại hệ thống tự động hóa chưa được tối ưu hoàn toàn.\n"
#             "Bạn có thể trực tiếp trải nghiệm các dịch vụ hỗ trợ tăng trưởng SNS có sẵn,\n"
#             "hoặc liên hệ admin để được hỗ trợ chính xác hơn:\n"
#             "📧 Email: hieutrungduongg@gmail.com\n"
#             "🔵 Fanpage Facebook: https://www.facebook.com/share/17wEK1REb2/?mibextid=wwXIfr"
#         )



from openai import OpenAI

MAX_AI_TURNS = 10


class saleAIService:

    def __init__(self, context_service):
        self.context_service = context_service

    # =========================
    # MAIN HANDLER
    # =========================
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
            return {"reply": self._fallback_message(lang)}

        # ===== CHECK TURN LIMIT =====
        turns = context.get("ai_count", 0)
        if turns >= MAX_AI_TURNS:
            return {"reply": self._fallback_message(lang)}

        sale_category = context.get("sale_category")
        platform = context.get("platform")
        if not sale_category or not platform:
            return {"reply": self._fallback_message(lang)}

        # ===== TURN STAGE (SERVER DECIDES) =====
        turn_stage = self._get_turn_stage(turns)

        # ===== BUILD PROMPT =====
        system_prompt = self._build_system_prompt(lang, turn_stage)
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
            print("💥 [AI] OpenAI ERROR:", repr(e))
            return {"reply": self._fallback_message(lang)}

        # ===== INCREASE TURN =====
        self.context_service.increase_ai_count(session_id)

        return {"reply": reply}

    # =========================
    # TURN STAGE (SERVER-SIDE)
    # =========================
    def _get_turn_stage(self, turns: int) -> str:
        if turns == 0:
            return "INTRO"
        if turns == 1:
            return "ORIENTATION"
        if turns == 2:
            return "BENEFIT"
        if turns == 3:
            return "SERVICE_INTRO"
        if turns <= 5:
            return "NARROW"
        if turns <= 7:
            return "CONFIRM"
        if turns == 8:
            return "CHATBOT_CORE"
        return "FAREWELL"

    # =========================
    # SYSTEM PROMPT (CORE – VI / EN / JP)
    # =========================
    def _build_system_prompt(self, lang: str, turn_stage: str) -> str:

        if lang == "EN":
            return f"""
You are a professional consultant and seller specializing in:
- Personal SNS growth
- Personal branding
- KOL / Creator support
- Overall SNS strategy
and consulting & sales chatbots.

GLOBAL RULES:
- Each reply MUST be 8–10 short lines.
- Polite, professional tone with light, respectful humor.
- No rambling, no repetition, no exaggerated promises.
- Examples MUST adapt to the user's consultation type and platform.

CONVERSATION CONTROL:
- Maximum 10 replies per session.
- Each reply MUST follow the objective of its current stage.
- Any question you ask MUST prepare for the NEXT stage of the flow.

OFF-TOPIC HANDLING:
- If the user asks something unrelated:
  + Respond with ONE very short, casual line (acknowledging emotion only).
  + DO NOT explain or open a new topic.
  + Immediately return to the current flow and continue selling or consulting.
  + Off-topic questions must NEVER consume a separate reply.

CURRENT STAGE: {turn_stage}

INTRO:
- Briefly introduce capability.
- Clearly state that we provide engagement & reach boosting services
  to help brands grow faster and sustainably.

ORIENTATION:
- Use concrete examples tailored to the consultation type.
- Ask ONLY one simple question that leads to BENEFIT stage.

BENEFIT:
- Explain realistic benefits with measurable outcomes.
- Prepare the ground for service introduction.

SERVICE_INTRO:
- Naturally introduce SNS growth services.

NARROW / CONFIRM:
- Narrow to the most suitable solution.
- Begin introducing chatbot service as a support tool.

CHATBOT_CORE:
- Emphasize chatbot consulting & sales as a core long-term solution.

FAREWELL:
- Short, polite goodbye.
- Restate chatbot as a key service.
- Do NOT ask new questions.
"""

        if lang == "JP":
            return f"""
あなたは以下分野に精通したプロのコンサルタント兼セールスです。
- 個人SNS成長
- パーソナルブランディング
- KOL / クリエイター支援
- SNS総合戦略
およびチャットボットによる相談・販売支援。

共通ルール:
- 1回の回答は8〜10行。
- 丁寧・プロフェッショナルで、軽いユーモアは可。
- 冗長・繰り返し・誇張は禁止。
- 例は必ず相談内容とプラットフォームに合わせる。

会話制御ルール:
- 最大10回の返信まで。
- 各返信は現在の段階目的に必ず従う。
- 質問する場合は、必ず次の段階につながる内容にする。

話題ズレ対応:
- 無関係な質問が来た場合:
  + 感情に合わせた短い一言のみ返す。
  + 説明・脱線は禁止。
  + 同じ返信内で必ず元の相談フローに戻る。
  + 話題ズレで返信を消費しない。

現在の段階: {turn_stage}

INTRO:
- 能力と提供サービスを簡潔に紹介。
- エンゲージメントとリーチ強化で成長を支援することを明示。

ORIENTATION:
- 相談内容に合った具体例を提示。
- 次段階につながる質問は1つのみ。

BENEFIT:
- 数値で測れる現実的な成果を説明。

SERVICE_INTRO:
- SNS成長支援を自然に案内。

NARROW / CONFIRM:
- 解決策を絞り、チャットボットを補助ツールとして紹介。

CHATBOT_CORE:
- チャットボットを中核サービスとして強調。

FAREWELL:
- 丁寧に締め、新しい質問は禁止。
"""

        # ===== VIETNAMESE (DEFAULT) =====
        return f"""
Bạn là tư vấn viên và seller chuyên nghiệp trong các mảng:
- Tăng trưởng SNS cá nhân
- Xây dựng thương hiệu cá nhân
- Hỗ trợ KOL / Creator
- Tư vấn mục tiêu SNS tổng thể
và triển khai chatbot tư vấn – bán hàng.

NGUYÊN TẮC BẮT BUỘC:
- Mỗi reply 8–10 dòng.
- Giọng lịch sự, chuyên nghiệp, thân thiện, có hài hước nhẹ.
- Không lan man, không lặp ý, không hứa hẹn phi thực tế.
- Ví dụ PHẢI linh động theo nhu cầu & nền tảng của khách.

KIỂM SOÁT CUỘC TRÒ CHUYỆN:
- Tối đa 10 reply cho mỗi phiên.
- Mỗi reply phải bám đúng mục tiêu của giai đoạn hiện tại.
- Mọi câu hỏi AI đặt ra PHẢI mở đường cho reply kế tiếp.

XỬ LÝ CÂU HỎI LỆCH CHỦ ĐỀ:
- Nếu người dùng hỏi không liên quan:
  + Trả lời 1 câu cực ngắn theo cảm xúc (cho qua, hên xui, tuỳ góc nhìn…).
  + Không giải thích, không mở chủ đề mới.
  + NGAY LẬP TỨC quay lại flow trong cùng reply.
  + Tuyệt đối không để câu hỏi lệch làm mất 1 lượt reply.

GIAI ĐOẠN HIỆN TẠI: {turn_stage}

INTRO:
- Giới thiệu ngắn gọn năng lực & dịch vụ.
- Khẳng định đang cung cấp dịch vụ đẩy mạnh tương tác,
  mở rộng tiếp cận để xây dựng thương hiệu nhanh và bền.

ORIENTATION:
- Định hướng bằng ví dụ thực tế phù hợp nhu cầu khách.
- Chỉ hỏi 1 câu để dẫn sang BENEFIT.

BENEFIT:
- Nêu lợi ích thực tế, có số liệu tương đối.
- Chuẩn bị cho bước giới thiệu dịch vụ.

SERVICE_INTRO:
- Dẫn nhẹ sang dịch vụ tăng trưởng SNS.

NARROW / CONFIRM:
- Thu hẹp giải pháp phù hợp nhất.
- Bắt đầu giới thiệu chatbot như công cụ hỗ trợ tư vấn & giữ khách.

CHATBOT_CORE:
- Nhấn mạnh chatbot tư vấn – bán hàng là dịch vụ cốt lõi.

FAREWELL:
- Chào tạm biệt lịch sự, không hỏi thêm câu mới.
"""

    # =========================
    # USER PROMPT (DATA ONLY)
    # =========================
    def _build_user_prompt(
        self,
        lang: str,
        sale_category: str,
        platform: str,
        user_message: str
    ) -> str:

        if lang == "JP":
            return f"""
文脈:
- 相談内容: {sale_category}
- プラットフォーム: {platform}

ユーザーの質問:
「{user_message}」
"""
        if lang == "EN":
            return f"""
Context:
- Consultation type: {sale_category}
- Platform: {platform}

Client question:
"{user_message}"
"""
        return f"""
Ngữ cảnh:
- Loại tư vấn: {sale_category}
- Nền tảng: {platform}

Câu hỏi của khách hàng:
"{user_message}"
"""

    # =========================
    # CONTACT & FALLBACK (GIỮ NGUYÊN)
    # =========================
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