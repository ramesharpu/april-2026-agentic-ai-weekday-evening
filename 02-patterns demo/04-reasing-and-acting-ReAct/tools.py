def calculator(expression: str):
    try:
        return eval(expression)
    except:
        return "Error: Invalid expression"
    
def search(query: str):
    knowledge = {
        "capital of france": "Paris",
        "largest planent": "Jupiter"
    }
    return knowledge.get(query.lower(), "No results found")
