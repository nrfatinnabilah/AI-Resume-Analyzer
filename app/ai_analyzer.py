import re

def normalize_text(text):
    # Remove spaces between single characters
    text = re.sub(r'(?<=\w) (?=\w)', '', text)

    return text.lower()

def extract_skills(text):

    skills_data = [
        "Python",
        "Java",
        "C++",
        "FastAPI",
        "Spring Boot",
        "SQL",
        "Machine Learning",
        "TensorFlow",
        "PyTorch",
        "Docker",
        "AWS"
    ]

    found_skills = []

    text_clean = normalize_text(text)

    for skill in skills_data:
        skill_clean = skill.lower().replace(" ", "")
        
        if skill_clean in text_clean:
            found_skills.append(skill)

    return found_skills