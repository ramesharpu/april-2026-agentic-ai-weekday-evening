from planner import Planner
from executor import Executor

class PlanningAgent:
    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()
        self.completed_steps = []
    
    def run(self, goal: str):
        print("Goal: ", goal)

        plan = self.planner.create_plan(goal)
        print("Plan: ")
        for i, step in enumerate(plan, 1):
            print(f"{i}. {step}")

        for step in plan:
            result = self.executor.execute(step)
            self.completed_steps.append(result)

        print("\n All the steps have been executed.")
        print("Completed Steps: ", self.completed_steps)

