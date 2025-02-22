from fastapi import FastAPI
from pydantic import BaseModel
from crew_ai_setup import process_user_prompt

app = FastAPI()

class UserPrompt(BaseModel):
    topic: str

@app.post("/ask-crew/")
async def ask_crew(user_prompt: UserPrompt):
    """
    Endpoint to process user queries via CrewAI agents.
    """
    response = process_user_prompt(user_prompt.topic)
    return {"response": response}
