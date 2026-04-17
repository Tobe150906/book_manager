import json
from pathlib import Path

BESTANDSNAAM = Path("data.json")

def load_books():
    if not BESTANDSNAAM.exists():
        return []
    try:
        with open(BESTANDSNAAM, "r") as bestand: 
            return json.load(bestand)
    except( json.JSONDecodeError, OSError):
        return []


def save_books(books):
    with open(BESTANDSNAAM, "w") as bestand:
        json.dump(books, bestand, indent = 4)



    
