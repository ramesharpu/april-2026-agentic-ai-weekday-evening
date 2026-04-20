from agents.planner import PlanningAgent
from agents.reseacher import ResearchAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent

class Coordinator:

    def __init__(self):
        self.planner = PlanningAgent()
        self.researcher = ResearchAgent()
        self.writer = WriterAgent()
        self.reviewer = ReviewerAgent()

    def run(self, goal: str):
        print(f"\n Goal: {goal}")

        # Step 1: Plan
        plan = self.planner.plan(goal)
        print(f"\n Plan: {plan}")

        # Step 2: Research
        research = self.researcher.research(goal)
        print(f"\n Research: {research}")

        # Step 3: Write
        draft = self.writer.write(research)
        print(f"\n Draft: {draft}")

        # Step 4: Review
        review = self.reviewer.review(draft)
        print(f"\n Review: {review}")

        return draft