from fastapi import FastAPI, UploadFile, File, Form
from app.resume_parser import extract_text
from app.ai_analyzer import extract_skills
from app.matcher import calculate_match


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API is running"
    }


@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    text = extract_text(file.file)

    skills = extract_skills(text)

    return {
        "filename": file.filename,
        "skills_detected": skills,
        "content": text
    }
    
@app.post("/match")
async def match_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    resume_text = extract_text(file.file)

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description)

    result = calculate_match(
        resume_skills,
        job_skills
    )

    return result