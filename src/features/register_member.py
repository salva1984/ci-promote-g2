from storage import find_by_id

def register_member(data, member_id, name):
    member_id = member_id.strip()
    name = name.strip()

    if not member_id:
        raise ValueError("Member id cannot be empty.")
    if not name:
        raise ValueError("Member name cannot be empty.")
    if find_by_id(data["members"], member_id) is not None:
        raise ValueError(f"Member id '{member_id}' is already registered.")

    member = {"id": member_id, "name": name}
    data["members"].append(member)
    return member
