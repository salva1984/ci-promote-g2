import json

ARCHIVO = "data.json"

MAX_PRESTAMOS = 3


def cargar(ruta=ARCHIVO):
    """Carga el estado desde el JSON; devuelve estructura vacía si no existe."""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"books": [], "members": [], "loans": []}


def guardar(data, ruta=ARCHIVO):
    """Escribe el estado al JSON."""
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def registrar_miembro(data, miembro_id, nombre):
    """Registra un miembro. Falla si el id ya está en uso."""
    if any(m["id"] == miembro_id for m in data["members"]):
        raise ValueError(f"El miembro '{miembro_id}' ya existe")
    data["members"].append({"id": miembro_id, "name": nombre})
    return data

