import re

def normalize_text(text):
    # Remove spaces between single characters
    text = re.sub(r'(?<=\w) (?=\w)', '', text)

    return text.lower()

def extract_skills(text):

    skills_database = [
        "Python",
        "Java",
        "Spring Boot",
        "SQL",
        "Machine Learning",
        "Docker",
        "FastAPI",
        "Azure",
        "REST API"
    ]

    detected = []

    text_lower = text.lower()

    for skill in skills_database:
        if skill.lower() in text_lower:
            detected.append(skill)

    return detected