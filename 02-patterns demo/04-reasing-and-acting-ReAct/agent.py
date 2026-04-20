from tools import calculator, search

class ReActAgent:
    def run(self, question: str):
        print(f"Question: {question}")

        # Thought - 1
        print("\n Thought: I need factual information.")
        print(" Action: search")
        observation = search("capital of france")
        print(f" Observation: {observation}")

        # Thought - 2
        print("\n Thought: I now know the answer.")
        final_answer = f"The capital of France is {observation}."
        return final_answer