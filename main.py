import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")

info_agent = Agent(
    role="Information Agent",
    goal="Give compelling information about a certain topic. Write in Czech language.",
    backstory="""
        You love to know information.  People love and hate you for it.  You win most of the
        quizzes at your local pub.
    """
)

critic_agent = Agent(
    role="Critic Agent",
    goal="Challenge the correctness and completeness of the information provided by the Information Agent",
    backstory="""
        You are a skeptic by nature. You enjoy finding flaws in arguments and pointing out missing details.
        Your goal is to ensure that the information provided is accurate and thorough.
    """
)

crazy_grandma_agent = Agent(
    role="Crazy Grandma Agent",
    goal="Provide a humorous and exaggerated take on the information provided by the Information Agent. Write in Czech language.",
    backstory="""
        You are a crazy grandma who loves to tell stories. You often exaggerate and add humor to your tales.
        Your goal is to entertain while still providing some level of information.
    """
)

task1 = Task(
    description="Tell me all about a wedding in the mountains.",
    expected_output="Give me a quick summary and then also give me 7 bullet points describing it.",
    agent=info_agent
)

task2 = Task(
    description="Evaluate the information provided by the Information Agent about the blue-ringed octopus.",
    expected_output="Provide a critique of the summary and bullet points, pointing out any inaccuracies or missing details.",
    agent=critic_agent
)

task3 = Task(
    description="Rewrite the full article based on crazy_grandma_agent ideas and make it more humorous.",
    expected_output="Humorous text that will appeal grandma.",
    agent=info_agent
)

task4 = Task(    
        description="Provide a humorous and exaggerated take on the information provided by the Information Agent.",
        expected_output="Provide a humorous and exaggerated story about the blue-ringed octopus.",
        agent=crazy_grandma_agent
    )

crew = Crew(
    agents=[info_agent, crazy_grandma_agent],
    tasks=[task1, task4, task3],
    verbose=True
)

result = crew.kickoff()

print("############")
print(result)

