from config import llm

def generate_summary(resume_data, jd_data):
    prompt = f"""
    Resume:
    {resume_data}

    Job Description:
    {jd_data}

    Generate a recruitment summary.
    """
    return llm.invoke(prompt)