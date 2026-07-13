from config import llm

def analyze_resume(resume_text):
    prompt = f"""
    You are an HR Resume Screening Assistant.

    Extract the following information from the resume:

    - Name
    - Skills
    - Education
    - Experience

    Return the result in a clear JSON format.

    Resume:
    {resume_text}
    """

    response = llm.invoke(prompt)
    return response.content