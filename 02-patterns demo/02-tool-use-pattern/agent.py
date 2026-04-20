from tools import calculator, search_tool

class Agent:
    def __init__(self):
        self.memory = []

    def decide_tool(self, task: str):
        if any(char.isdigit() for char in task):
            return "calculator"
        return "search_tool"
    
    def act(self, task: str):
        tool = self.decide_tool(task)

        if tool == "calculator":
            expression = task.split("calculate")[-1].strip()
            results = calculator(expression)
            return f"Used calculator tool -> {results}"
        
        if tool == "search_tool":
            query = task.replace("what is", "").strip()
            results = search_tool(query)
            return f"Used search tool -> {results}"