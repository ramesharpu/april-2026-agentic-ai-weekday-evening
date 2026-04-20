class Planner:
    
    def create_plan(self, goal):    
        if "presentation" in goal.lower():
            return[
                "understand the topic",
                "create an outline",
                "prepare slides",
                "review and practice"
            ]
        return [
            "understand the goal",
            "break it into smaller steps",
            "execute each step",
            "verify the results"
        ]