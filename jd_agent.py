from config import llm

def analyze_jd(job_description):
    prompt = f"""
    Extract:
    - Required skills
    - Experience
    - Education

    Job Description:
    {job_description}
    """
    return llm.invoke(prompt)