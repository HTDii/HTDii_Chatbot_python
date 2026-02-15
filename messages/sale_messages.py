# messages/sale_messages.py

SALE_INTRO = {
    "VI": {
        "reply": "🛒 Chúng tôi cung cấp các giải pháp tiếp thị số giúp hỗ trợ tăng trưởng "
                 "và tối ưu hiệu quả hoạt động trên các nền tảng mạng xã hội."
    },
    "EN": {
        "reply": "🛒 We provide digital marketing solutions to support growth and "
                 "optimize performance on social media platforms."
    },
    "JP": {
        "reply": "🛒 当社は、SNSプラットフォーム上での成長支援および "
                 "パフォーマンス最適化を目的としたデジタルマーケティング施策を提供しています。"
    }
}

SALE_MENU = {
    "VI": {
        "options": [
            {"label": "📈 Tăng trưởng SNS cá nhân", "value": "SNS_PERSONAL"},
            {"label": "🏷️ Xây dựng thương hiệu cá nhân", "value": "BRAND_BUILDING"},
            {"label": "🎯 Hỗ trợ KOL / Creator", "value": "KOL_SUPPORT"},
            {"label": "🧭 Tư vấn mục tiêu SNS tổng quát", "value": "GENERAL_GOAL"},
        ]
    },
    "EN": {
        "options": [
            {"label": "📈 Personal SNS growth", "value": "SNS_PERSONAL"},
            {"label": "🏷️ Personal brand building", "value": "BRAND_BUILDING"},
            {"label": "🎯 KOL / Creator support", "value": "KOL_SUPPORT"},
            {"label": "🧭 General SNS goal consultation", "value": "GENERAL_GOAL"},
        ]
    },
    "JP": {
        "options": [
            {"label": "📈 個人SNS成長支援", "value": "SNS_PERSONAL"},
            {"label": "🏷️ 個人ブランド構築", "value": "BRAND_BUILDING"},
            {"label": "🎯 KOL・クリエイター支援", "value": "KOL_SUPPORT"},
            {"label": "🧭 SNS全体目標の相談", "value": "GENERAL_GOAL"},
        ]
    },
}

SALE_CATEGORY_REPLY = {
    "SNS_PERSONAL": {
        "VI": {
            "reply": "Chúng tôi tập trung vào việc tối ưu nội dung, lịch đăng tải và "
                     "các công cụ hỗ trợ tăng trưởng phù hợp với chính sách nền tảng."
        },
        "EN": {
            "reply": "We focus on content optimization, posting schedules and "
                     "platform-compliant growth support tools."
        },
        "JP": {
            "reply": "コンテンツ最適化、投稿スケジュール、および "
                     "プラットフォーム規約に準拠した成長支援を行います。"
        }
    },
    "BRAND_BUILDING": {
        "VI": {
            "reply": "Dịch vụ xây dựng thương hiệu cá nhân giúp định vị hình ảnh, "
                     "thông điệp và phong cách nội dung một cách bền vững."
        },
        "EN": {
            "reply": "Personal brand building services help define positioning, "
                     "messaging and content style sustainably."
        },
        "JP": {
            "reply": "個人ブランド構築サービスでは、イメージやメッセージ、 "
                     "コンテンツスタイルを長期的に最適化します。"
        }
    },
    "KOL_SUPPORT": {
        "VI": {
            "reply": "Hỗ trợ Creator/KOL phát triển kênh thông qua phân tích dữ liệu "
                     "và chiến lược nội dung dài hạn."
        },
        "EN": {
            "reply": "We support creators and KOLs through data analysis "
                     "and long-term content strategies."
        },
        "JP": {
            "reply": "データ分析および長期的なコンテンツ戦略を通じて "
                     "KOL・クリエイターを支援します。"
        }
    },
    "GENERAL_GOAL": {
        "VI": {
            "reply": "Hãy chia sẻ mục tiêu của bạn, chúng tôi sẽ đề xuất "
                     "hướng triển khai phù hợp."
        },
        "EN": {
            "reply": "Please share your goal and we will propose "
                     "a suitable approach."
        },
        "JP": {
            "reply": "目標を教えていただければ、最適な進め方をご提案します。"
        }
    },
}

SALE_PLATFORM_OPTIONS = {
    "VI": {
        "options": [
            {"label": "TikTok", "value": "TIKTOK"},
            {"label": "Facebook", "value": "FACEBOOK"},
            {"label": "Telegram", "value": "TELEGRAM"},
            {"label": "Instagram", "value": "INSTAGRAM"},
            {"label": "YouTube", "value": "YOUTUBE"},
            {"label": "⬅️ Quay lại", "value": "BACK_TO_SALE_MENU"},
        ]
    },
    "EN": {
        "options": [
            {"label": "TikTok", "value": "TIKTOK"},
            {"label": "Facebook", "value": "FACEBOOK"},
            {"label": "Telegram", "value": "TELEGRAM"},
            {"label": "Instagram", "value": "INSTAGRAM"},
            {"label": "YouTube", "value": "YOUTUBE"},
            {"label": "⬅️ Back", "value": "BACK_TO_SALE_MENU"},
        ]
    },
    "JP": {
        "options": [
            {"label": "TikTok", "value": "TIKTOK"},
            {"label": "Facebook", "value": "FACEBOOK"},
            {"label": "Telegram", "value": "TELEGRAM"},
            {"label": "Instagram", "value": "INSTAGRAM"},
            {"label": "YouTube", "value": "YOUTUBE"},
            {"label": "⬅️ 戻る", "value": "BACK_TO_SALE_MENU"},
        ]
    },
}

SALE_PLATFORM_REPLY = {
    "VI": {
        "reply": "Chúng tôi tập trung vào tối ưu nội dung, phân tích hành vi người dùng "
                 "và các công cụ hỗ trợ tăng trưởng minh bạch, tuân thủ điều khoản sử dụng."
    },
    "EN": {
        "reply": "We focus on content optimization, audience behavior analysis "
                 "and transparent growth support tools that comply with platform policies."
    },
    "JP": {
        "reply": "コンテンツ最適化、ユーザー行動分析、および "
                 "利用規約に準拠した透明性のある成長支援を行います。"
    }
}

SALE_CTA_OPTIONS = {
    "VI": {
        "options": [
            {"label": "📩 Nhận tư vấn chi tiết", "value": "REQUEST_CONSULT"},
            {"label": "⬅️ Quay lại menu", "value": "BACK_TO_SALE_MENU"},
        ]
    },
    "EN": {
        "options": [
            {"label": "📩 Get detailed consultation", "value": "REQUEST_CONSULT"},
            {"label": "⬅️ Back to menu", "value": "BACK_TO_SALE_MENU"},
        ]
    },
    "JP": {
        "options": [
            {"label": "📩 詳細相談を受ける", "value": "REQUEST_CONSULT"},
            {"label": "⬅️ メニューに戻る", "value": "BACK_TO_SALE_MENU"},
        ]
    },
}

SALE_FALLBACK = {
    "VI": {
        "reply": "Tôi đã ghi nhận yêu cầu của bạn. Bạn có thể chọn một mục tư vấn."
    },
    "EN": {
        "reply": "I have noted your request. Please select a consultation option."
    },
    "JP": {
        "reply": "ご要望を受け取りました。相談項目を選択してください。"
    }
}