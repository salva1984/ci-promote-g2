"""Shared storage for CaféLibro.

Loads and saves the library state (books, members, loans) from a JSON file
at the repository root. This is plumbing shared by every feature; it is not
one of the five graded features.
"""
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
    """Return the library state as a dict. Creates a seeded file if missing."""
    if not os.path.exists(DATA_FILE):
        save_data(SEED)
        return SEED
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    """Write the library state back to disk."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def find_by_id(items, item_id):
    """Return the first item whose 'id' matches, or None. Reused by features."""
    for item in items:
        if item["id"] == item_id:
            return item
    return None