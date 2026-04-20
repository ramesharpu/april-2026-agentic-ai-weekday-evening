from agent import ReActAgent

agent = ReActAgent()

question = "What is the capital of France?"
answer = agent.run(question)
print(f"\nFinal Answer: {answer}")