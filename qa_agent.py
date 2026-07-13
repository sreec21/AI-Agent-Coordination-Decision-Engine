from config import llm

def answer_question(resume, question):
    prompt = f"""
    Resume:
    {resume}

    Question:
    {question}
    """
    return llm.invoke(prompt)