from pypdf import PdfReader
import re


def clean_text(text):

    # Normalize spaces
    text = re.sub(r'\s+', ' ', text)


    # Fix common PDF character spacing only
    replacements = {
        "P y t h o n": "Python",
        "F a s t A P I": "FastAPI",
        "J a v a": "Java",
        "S Q L": "SQL",
        "A z u r e": "Azure",
        "A P I": "API",
        "D o c k e r": "Docker",
    }


    for old, new in replacements.items():
        text = text.replace(old, new)


    return text.strip()



def extract_text(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += " " + page_text


    return clean_text(text)