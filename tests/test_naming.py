from ai_lint.checks.naming import NamingCheck


def test_ignores_snake_case():
    source = "def good_name():\n    good_var = 1\n    return good_var"
    issues = NamingCheck().run(source)
    assert issues == []


def test_flags_camel_case_function():
    source = "def badName():\n    return 1"
    issues = NamingCheck().run(source)
    assert len(issues) == 1
    assert "badName" in issues[0].message


def test_flags_camel_case_variable():
    source = "myBadVar = 1"
    issues = NamingCheck().run(source)
    assert len(issues) == 1
    assert "myBadVar" in issues[0].message