import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from .user_context import user_context
from .sales_prompt import SALES_BOT_PROMPT
from .product_knowledge import COMBINED_KNOWLEDGE

report_json = user_context.get("report")
load_dotenv()

MODEL = os.getenv("GOOGLE_GENAI_MODEL", "gemini-1.5-pro")

FINAL_SALES_BOT_PROMPT = SALES_BOT_PROMPT + COMBINED_KNOWLEDGE

root_agent = Agent(
    name="beyond_vitals_sales_bot",
    description="A helpful Sales Assistant for Beyond Vitals' health insights platform",
    tools=[],
    model="gemini-2.0-flash",
    instruction = FINAL_SALES_BOT_PROMPT,
)