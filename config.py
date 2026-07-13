import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

MODEL = "gemini-2.5-flash-lite"

print("API:", os.getenv("GOOGLE_API_KEY"))
print("MODEL:", MODEL)

llm = ChatGoogleGenerativeAI(
    model=MODEL,
    temperature=0
)