from agent import Agent
from reflection import Reflector

Task = "Explain why AI is powerful."

agent = Agent()
reflector = Reflector()

max_attempts = 3

for step in range(max_attempts):
    print(f"\n ---- Itreation {step + 1} ----")

    output = agent.act(Task)
    print(f"Agent output: {output}")

    feedback = reflector.reflect(Task, output)
    print(f"Reflector feedback: {feedback}")

    if feedback == "good answer":
        print("Task is complete.")
        break