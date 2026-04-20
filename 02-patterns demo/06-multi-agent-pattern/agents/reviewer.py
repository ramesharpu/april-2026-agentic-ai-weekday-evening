class ReviewerAgent:

    def review(self, text: str):
        if (len(text) < 50):
            return "Needs more detail."
        return "Approved"