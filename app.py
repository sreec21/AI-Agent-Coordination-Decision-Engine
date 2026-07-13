from agents.resume_agent import analyze_resume
from agents.jd_agent import analyze_jd
from agents.qa_agent import answer_question
from agents.response_agent import generate_summary

resume = open("resume.txt").read()
jd = open("job.txt").read()

resume_result = analyze_resume(resume)
jd_result = analyze_jd(jd)

summary = generate_summary(resume_result, jd_result)

print(summary)