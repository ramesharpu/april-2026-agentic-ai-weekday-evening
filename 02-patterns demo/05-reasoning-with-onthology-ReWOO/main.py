from agent import OntologyAgent

agent = OntologyAgent()

questions = [
    "What is the capital of France?",
    "What is the population of France?",
    "What is the capital and population of France?",
    "Explain quantum mechanics."
]

for q in questions:
    answer = agent.run(q)
    print(f"Answer: {answer}\n")