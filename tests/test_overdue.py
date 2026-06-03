from overdue import report_overdue


def test_report_overdue_returns_only_overdue_loans():
    loans = [
        {"name": "Ana", "object_loaned": "Libro A", "due_date": "2026-06-01"},
        {"name": "Luis", "object_loaned": "Libro B", "due_date": "2026-06-10"},
    ]

    overdue = report_overdue("2026-06-03", loans)

    assert len(overdue) == 1
    assert overdue[0]["name"] == "Ana"
    assert overdue[0]["object_loaned"] == "Libro A"