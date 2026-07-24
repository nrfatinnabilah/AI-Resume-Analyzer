def calculate_match(resume_skills, job_description):

    job_skill_list = extract_job_skills(job_description)

    matched = []
    missing = []


    for skill in job_skill_list:

        if skill.lower() in [
            x.lower() for x in resume_skills
        ]:
            matched.append(skill)

        else:
            missing.append(skill)


    score = round(
        len(matched) / len(job_skill_list) * 100,
        2
    )


    return {
        "match_percentage": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "message": get_message(score)
    }



def extract_job_skills(job_description):

    skill_database = [
        "Python",
        "Java",
        "Spring Boot",
        "SQL",
        "Machine Learning",
        "Docker",
        "Azure",
        "FastAPI",
        "REST API",
        "AWS",
        "Kubernetes",
        "Git",
        "Agile",
        "PostgreSQL",
        "MySQL",
        "CI/CD",
        "Microservices"
    ]


    detected = []

    text = job_description.lower()


    for skill in skill_database:

        if skill.lower() in text:
            detected.append(skill)


    return detected



def get_message(score):

    if score >= 80:
        return "Excellent match"

    elif score >= 60:
        return "Good match"

    elif score >= 40:
        return "Moderate match"

    else:
        return "Low match"