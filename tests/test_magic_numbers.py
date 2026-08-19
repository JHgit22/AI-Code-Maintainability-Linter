from ai_lint.checks.magic_numbers import MagicNumberCheck


def test_ignores_allowed_numbers():
    source = "x = 1\ny = 0\nz = 2"
    issues = MagicNumberCheck().run(source)
    assert issues == []


def test_flags_magic_number():
    source = "timeout = 47"
    issues = MagicNumberCheck().run(source)
    assert len(issues) == 1
    assert "47" in issues[0].message


def test_ignores_booleans():
    source = "is_active = True"
    issues = MagicNumberCheck().run(source)
    assert issues == []