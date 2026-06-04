import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data.json")

SEED = {
    "books": [
        {"id": "B001", "title": "Cien Años de Soledad"},
        {"id": "B002", "title": "Don Quijote de la Mancha"},
        {"id": "B003", "title": "La Casa de los Espíritus"},
        {"id": "B004", "title": "Rayuela"},
        {"id": "B005", "title": "Pedro Páramo"},
    ],
    "members": [],
    "loans": [],
}

def load_data():
    if not os.path.exists(DATA_FILE):
        save_data(SEED)
        return SEED
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def find_by_id(items, item_id):
    for item in items:
        if item["id"] == item_id:
            return item
    return None
