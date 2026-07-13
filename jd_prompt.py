from langchain_core.prompts import PromptTemplate

jd_prompt = PromptTemplate.from_template("""
You are an HR Job Description Analyzer.

Extract:

- Job Title
- Required Skills
- Preferred Skills
- Experience Required
- Education Required
- Responsibilities

Return the response as valid JSON.

Job Description:
{job_description}
""")