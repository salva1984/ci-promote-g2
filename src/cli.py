"""CLI principal del proyecto."""

import os
import json

ARCHIVO = "data.json"

if not os.path.exists(ARCHIVO):
    data = {"books": [], "members": [], "loans": []}

    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
