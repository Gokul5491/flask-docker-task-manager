from app import app


def test_app_exists():
    assert app is not None


def test_routes():
    routes = [rule.rule for rule in app.url_map.iter_rules()]

    assert "/" in routes
    assert "/add" in routes
    assert "/delete/<int:task_id>" in routes