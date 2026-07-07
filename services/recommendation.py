QUESTIONS = [
    {"id": "math_score", "text": "علاقه و توانایی‌ات در ریاضی چقدر است؟", "category": "math"},
    {"id": "science_interest", "text": "علوم تجربی (فیزیک، شیمی، زیست) چقدر برایت جذاب است؟", "category": "science"},
    {"id": "social_interest", "text": "علوم انسانی و مطالعات اجتماعی را چقدر دوست داری؟", "category": "social"},
    {"id": "creative_interest", "text": "فعالیت‌های خلاقانه (نقاشی، موسیقی، طراحی) چقدر جذاب‌اند؟", "category": "creative"},
    {"id": "analytical_thinking", "text": "حل مسائل پیچیده و تحلیل داده‌ها را چقدر دوست داری؟", "category": "analytical"},
    {"id": "reading_interest", "text": "مطالعه کتاب و مقاله را چقدر دوست داری؟", "category": "reading"},
    {"id": "leadership", "text": "رهبری تیم و مدیریت پروژه را چقدر دوست داری؟", "category": "leadership"},
    {"id": "technology_interest", "text": "فناوری، برنامه‌نویسی و کامپیوتر چقدر برایت جذاب است؟", "category": "technology"},
    {"id": "helping_others", "text": "کمک به دیگران و کارهای انسان‌دوستانه را چقدر دوست داری؟", "category": "helping"},
    {"id": "physical_activity", "text": "فعالیت‌های بدنی و ورزشی را چقدر دوست داری؟", "category": "physical"},
    {"id": "language_skill", "text": "زبان‌های خارجی و ارتباطات کلامی را چقدر دوست داری؟", "category": "language"},
    {"id": "detail_oriented", "text": "کارهای دقیق و جزئی‌نگر (حسابداری، آزمایشگاه) را چقدر دوست داری؟", "category": "detail"},
    {"id": "public_speaking", "text": "سخنرانی و ارائه در جمع را چقدر دوست داری؟", "category": "speaking"},
    {"id": "research_interest", "text": "تحقیق و پژوهش علمی را چقدر دوست داری؟", "category": "research"},
    {"id": "business_interest", "text": "کسب‌وکار، بازاریابی و فروش را چقدر دوست داری؟", "category": "business"},
]

MAJORS = {
    "engineering": {
        "title": "مهندسی",
        "description": "رشته‌های مهندسی (برق، کامپیوتر، مکانیک، عمران) مناسب علاقه‌مندان به ریاضی، فناوری و حل مسئله.",
    },
    "medicine": {
        "title": "پزشکی و علوم پزشکی",
        "description": "رشته‌های پزشکی، دندانپزشکی، داروسازی و پرستاری برای کسانی که به علوم زیستی و کمک به مردم علاقه دارند.",
    },
    "humanities": {
        "title": "علوم انسانی",
        "description": "رشته‌های حقوق، روانشناسی، علوم تربیتی و جامعه‌شناسی برای علاقه‌مندان به مطالعه و تحلیل اجتماعی.",
    },
    "arts": {
        "title": "هنر و طراحی",
        "description": "رشته‌های هنرهای تجسمی، معماری، موسیقی و طراحی گرافیک برای افراد خلاق.",
    },
    "business": {
        "title": "مدیریت و کسب‌وکار",
        "description": "رشته‌های مدیریت، حسابداری، بازرگانی و اقتصاد برای علاقه‌مندان به رهبری و کسب‌وکار.",
    },
    "experimental": {
        "title": "رشته تجربی (دبیرستان)",
        "description": "گرایش علوم تجربی در دبیرستان مناسب علاقه‌مندان به زیست، شیمی و پزشکی.",
    },
    "math_physics": {
        "title": "رشته ریاضی‌فیزیک (دبیرستان)",
        "description": "گرایش ریاضی‌فیزیک در دبیرستان مناسب علاقه‌مندان به ریاضیات و مهندسی.",
    },
    "humanities_field": {
        "title": "رشته انسانی (دبیرستان)",
        "description": "گرایش علوم انسانی در دبیرستان مناسب علاقه‌مندان به ادبیات، تاریخ و علوم اجتماعی.",
    },
}


def _get(answers: dict, key: str) -> float:
    return float(answers.get(key, 5))


def recommend_majors(answers: dict) -> list[dict]:
    scores = {}

    scores["engineering"] = (
        _get(answers, "math_score") * 8
        + _get(answers, "technology_interest") * 9
        + _get(answers, "analytical_thinking") * 8
        + _get(answers, "science_interest") * 5
    )

    scores["medicine"] = (
        _get(answers, "science_interest") * 9
        + _get(answers, "helping_others") * 8
        + _get(answers, "detail_oriented") * 6
        + _get(answers, "research_interest") * 5
    )

    scores["humanities"] = (
        _get(answers, "social_interest") * 9
        + _get(answers, "reading_interest") * 8
        + _get(answers, "language_skill") * 7
        + _get(answers, "public_speaking") * 5
    )

    scores["arts"] = (
        _get(answers, "creative_interest") * 10
        + _get(answers, "physical_activity") * 3
        + _get(answers, "public_speaking") * 4
    )

    scores["business"] = (
        _get(answers, "business_interest") * 9
        + _get(answers, "leadership") * 8
        + _get(answers, "public_speaking") * 6
        + _get(answers, "math_score") * 4
    )

    scores["experimental"] = (
        _get(answers, "science_interest") * 10
        + _get(answers, "research_interest") * 6
        + _get(answers, "detail_oriented") * 5
    )

    scores["math_physics"] = (
        _get(answers, "math_score") * 10
        + _get(answers, "analytical_thinking") * 8
        + _get(answers, "technology_interest") * 5
    )

    scores["humanities_field"] = (
        _get(answers, "social_interest") * 10
        + _get(answers, "reading_interest") * 7
        + _get(answers, "language_skill") * 6
    )

    max_score = max(scores.values()) if scores else 1
    results = []
    for key, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        major = MAJORS[key]
        results.append({
            "key": key,
            "title": major["title"],
            "description": major["description"],
            "match_percent": round((score / max_score) * 100),
        })

    return results
