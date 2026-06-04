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


def test_menu_unknown_option_then_exit(monkeypatch, capsys):
    monkeypatch.setattr(menu, "ACTIONS", {})
    called = {"load": False}

    def fake_load():
        called["load"] = True
        return {}

    monkeypatch.setattr(menu, "load_data", fake_load)
    inputs = iter(["9", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    menu.main()

    out = capsys.readouterr().out
    assert "Unknown option." in out
    assert called["load"] is False


def test_menu_action_error_printed(monkeypatch, capsys):
    def action(_data):
        raise ValueError("Boom")

    monkeypatch.setattr(menu, "ACTIONS", {"1": ("Do", action)})
    monkeypatch.setattr(menu, "load_data", lambda: {"ok": True})
    inputs = iter(["1", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    menu.main()

    out = capsys.readouterr().out
    assert "Error: Boom" in out


def test_menu_displays_actions(monkeypatch, capsys):
    monkeypatch.setattr(
        menu,
        "ACTIONS",
        {"1": ("Do", lambda _data: None), "2": ("Other", lambda _data: None)},
    )
    inputs = iter(["0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    menu.main()

    out = capsys.readouterr().out
    assert "1. Do" in out
    assert "2. Other" in out
