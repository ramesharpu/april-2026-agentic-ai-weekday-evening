class Agent:
    def __init__(self):
        self.attempt = 0

    def act(self, task: str) -> str:
        self.attempt += 1

        if self.attempt == 1:
            return "AI is cool."
        elif self.attempt == 2:
            return "AI is cool it can learn from data."
        else:
            return(
                "Artificial Intelligence is powerful because"
                " it can learn patterns from data, make decisions, "
                "and imporve over time using feedback."
            )