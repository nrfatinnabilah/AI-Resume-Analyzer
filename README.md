# AI Resume Analyzer - Project Summary

AI Resume Analyzer is an AI-powered ATS (Applicant Tracking System) that analyzes resumes and compares them with job descriptions to evaluate candidate suitability.

The system is built using Python and FastAPI. It allows users to upload a PDF resume, extracts the resume content using PyPDF, detects relevant technical skills, and compares them with the required skills from a given job description.

Initially, the project used TF-IDF and cosine similarity to compare the full resume text with job descriptions. However, the results were inaccurate because resumes contain unrelated information such as education, projects, and personal details. The approach was improved by implementing skill-based matching, where technical skills are extracted from both the resume and job description before calculating the compatibility score.

The system currently provides:
- Resume PDF upload
- Resume text extraction and preprocessing
- Technical skill detection
- Job description skill analysis
- Resume-job match percentage calculation
- Matched skills identification
- Missing skills detection

Technologies used:
- Python
- FastAPI
- PyPDF
- Scikit-learn
- NLP techniques
- Git & GitHub

Future improvements include implementing AI embeddings for semantic matching, skill synonym detection, weighted skill scoring, and AI-generated resume improvement recommendations.

This project demonstrates the application of backend development, natural language processing, and AI techniques to build an intelligent recruitment assistance system.
