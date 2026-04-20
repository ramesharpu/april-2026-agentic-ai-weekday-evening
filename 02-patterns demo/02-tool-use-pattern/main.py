from agent import Agent

agent = Agent()

tasks = [
    "calculate 3 + 5 * 2",
    "what is the capital of France",
    "what is ai"
]

for task in tasks:
    print("\n Task: ", task)
    reponse = agent.act(task)
    print("Response: ", reponse)