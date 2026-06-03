import json
import os

archivo = "data.json"

if not os.path.exists(archivo):
    datos_iniciales = {
        "books": [],
        "members": [],
        "loans": []
    }

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos_iniciales, f, indent=4, ensure_ascii=False)

    print("Se inicializó con la base de datos")
else:
    print("La base de datos ya existe en un json.")