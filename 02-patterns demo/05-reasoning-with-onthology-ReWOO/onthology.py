ONTOLOGY = {
    "Country":{
        "attributes": ["capital", "population"]
    },
    "Capital":{
        "attributes": [ "population"]
    },
    "France": {
        "type": "Country",
        "capital": "Paris",
        "population": "67 million"
    },
    "Paris": {
        "type": "Capital",
        "population": "2.1 million"
    }
}