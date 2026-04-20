class Reflector:

    def reflect(self, task: str, output: str) -> str:
        if len(output) < 5:
            return "too short, needs more detail"
        if "because" not in output:
            return "explaination lacks reasoning"
        return "good answer"