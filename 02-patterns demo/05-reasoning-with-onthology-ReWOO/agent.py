from reasonor import OntologyReasoner

class OntologyAgent:

    def __init__(self):
        self.reasoner = OntologyReasoner()

    def run(self, question: str):
        print(f"Question: {question}")
        result = self.reasoner.answer(question)
        return result