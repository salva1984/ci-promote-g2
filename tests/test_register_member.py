
import pytest

from features.register_member import register_member


def fresh_data():
    return {"books": [], "members": [], "loans": []}


def test_register_adds_member():
    data = fresh_data()
    member = register_member(data, "M001", "Ada")
    assert member == {"id": "M001", "name": "Ada"}
    assert data["members"] == [{"id": "M001", "name": "Ada"}]


def test_register_trims_whitespace():
    data = fresh_data()
    member = register_member(data, "  M002 ", "  Linus ")
    assert member == {"id": "M002", "name": "Linus"}


def test_duplicate_id_raises():
    data = fresh_data()
    register_member(data, "M001", "Ada")
    with pytest.raises(ValueError):
        register_member(data, "M001", "Grace")


def test_empty_id_raises():
    data = fresh_data()
    with pytest.raises(ValueError):
        register_member(data, "  ", "Ada")


def test_empty_name_raises():
    data = fresh_data()
    with pytest.raises(ValueError):
        register_member(data, "M001", "  ")
