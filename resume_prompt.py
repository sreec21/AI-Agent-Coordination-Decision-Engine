from langchain_core.prompts import PromptTemplate

resume_prompt = PromptTemplate.from_template("""
You are an HR Resume Screening Assistant.

Extract the following information from the candidate's resume:

- Full Name
- Email
- Phone Number
- Skills
- Education
- Experience
- Projects
- Certifications

Return the response as valid JSON.

Resume:
{resume}
""")