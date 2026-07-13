from langchain_core.prompts import PromptTemplate

response_prompt = PromptTemplate.from_template("""
You are an HR Recruitment Expert.

Resume Details:
{resume}

Job Description:
{job_description}

Generate:

1. Candidate Summary
2. Matching Skills
3. Missing Skills
4. Recommendation

Keep the response professional.
""")