from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match(resume_text, job_description):

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )

    score = round(similarity[0][0] * 100, 2)


    return {
        "match_percentage": score,
        "message": get_message(score)
    }



def get_message(score):

    if score >= 80:
        return "Excellent match"

    elif score >= 60:
        return "Good match"

    elif score >= 40:
        return "Moderate match"

    else:
        return "Low match"