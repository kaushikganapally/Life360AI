import logging
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai.crews.crew_output import CrewOutput
from fastapi.responses import PlainTextResponse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

# Retrieve Mistral API details from the .env file
api_key = os.getenv("MISTRAL_API_KEY")
model_name = os.getenv("MISTRAL_MODEL_NAME")

if not api_key or not model_name:
    raise ValueError("Missing required environment variables. Check .env file.")

# Initialize LLM once and reuse it
mistral_llm = LLM(
    api_key=api_key,
    model=f"mistral/{model_name}"
)

# Define agents with the shared LLM instance
planner = Agent(
    role="Content Planner",
    goal="Create engaging and factually accurate content on {topic}",
    backstory="An expert planner curating strategic content...",
    allow_delegation=False,
    verbose=True,
    llm=mistral_llm  # Pass the shared LLM instance
)

writer = Agent(
    role="Content Writer",
    goal="Develop insightful content to engage stakeholders on {topic}",
    backstory="A content specialist crafting compelling narratives...",
    allow_delegation=False,
    verbose=True,
    llm=mistral_llm  # Pass the shared LLM instance
)

editor = Agent(
    role="Editor",
    goal="Ensure clarity and alignment with business goals",
    backstory="An experienced editor refining content for maximum impact...",
    allow_delegation=False,
    verbose=True,
    llm=mistral_llm  # Pass the shared LLM instance
)

# Define tasks
plan_task = Task(
    description="Develop a content plan for {topic} considering industry trends.",
    expected_output="Comprehensive content plan with key strategic insights.",
    agent=planner,
    name="plan_task"  # Assign a name to use as a key
)

write_task = Task(
    description="Write detailed content based on the content plan for {topic}.",
    expected_output="A well-written content outline ready for review.",
    agent=writer,
    name="write_task"  # Assign a name to use as a key
)

edit_task = Task(
    description="Review and refine the content to align with business objectives.",
    expected_output="Polished and business-aligned content.",
    agent=editor,
    name="edit_task"  # Assign a name to use as a key
)

# Ensure crew is correctly initialized with named tasks
life360_crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan_task, write_task, edit_task],
    verbose=True
)

def process_user_prompt(topic: str):
    """
    Process user input through the AI agents and return the formatted response.
    """
    results = life360_crew.kickoff(inputs={"topic": topic})

    if isinstance(results, CrewOutput):
        tasks_output = results.tasks_output

        if isinstance(tasks_output, list):
            final_review = None

            for task in tasks_output:
                if hasattr(task, 'name') and hasattr(task, 'raw'):
                    if task.name == "edit_task":  # Assuming "edit_task" contains the final review
                        final_review = task.raw

            if final_review:
                return PlainTextResponse(content=final_review)

    return PlainTextResponse(content="No final review available.")
