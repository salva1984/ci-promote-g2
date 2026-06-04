import menu

def test_menu_exit_immediately(monkeypatch, capsys):
    monkeypatch.setattr(menu, "ACTIONS", {})
    inputs = iter(["0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    menu.main()

    out = capsys.readouterr().out
    assert "Goodbye." in out

def test_menu_runs_action(monkeypatch):
    called = {}

    def action(data):
        called["data"] = data

    monkeypatch.setattr(menu, "ACTIONS", {"1": ("Do", action)})
    monkeypatch.setattr(menu, "load_data", lambda: {"ok": True})
    inputs = iter(["1", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    menu.main()

    assert called["data"] == {"ok": True}
