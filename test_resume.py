import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.resume_agent import analyze_resume

resume = """
John Doe

Email: john.doe@gmail.com

Education:
B.Tech in Computer Science

Experience:
Software Engineer at ABC Technologies (2 years)

Skills:
Python
SQL
Flask
Machine Learning

Projects:
Employee Management System

Certifications:
Google Data Analytics
"""

result = analyze_resume(resume)

print("===== Resume Analysis =====")
print(result)