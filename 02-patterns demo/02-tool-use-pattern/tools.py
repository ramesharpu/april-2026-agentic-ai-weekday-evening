
def calculator(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception:
        return "Calculation error"

def search_tool(query: str) -> str:
    fake_result = {
        "the capital of france": "Paris",
        "ai": "AI stands for Artificial Intelligence."
    }
    return fake_result.get(query.lower(), "No results found")