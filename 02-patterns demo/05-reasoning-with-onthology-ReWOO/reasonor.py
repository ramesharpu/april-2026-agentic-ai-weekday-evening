from onthology import ONTOLOGY

class OntologyReasoner:

    def answer(self, question: str):
        q = question.lower()

        if "france" in q:
            country = ONTOLOGY["France"]

            if "capital" in q and "population" in q:
                capital = country["capital"]
                capital_population = ONTOLOGY[capital]["population"]
                return capital, capital_population
            
            if "capital" in q:
                return country["capital"]
            
            if "population"in q:
                return country["population"]
            
        return "Answer not found in the ontology."