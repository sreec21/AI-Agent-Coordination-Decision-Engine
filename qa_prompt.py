from langchain_core.prompts import PromptTemplate

qa_prompt = PromptTemplate.from_template("""
You are an HR Recruitment Assistant.

Answer the recruiter's question using ONLY the resume below.

If the answer is not present, reply:

"Information Not Available"

Resume:
{resume}

Question:
{question}
""")