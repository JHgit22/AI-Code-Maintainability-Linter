from ai_lint.checks.nesting_depth import NestingDepthCheck


def test_ignores_shallow_nesting():
    source = """
if True:
    for x in range(3):
        print(x)
"""
    issues = NestingDepthCheck(max_depth=3).run(source)
    assert issues == []


def test_flags_deep_nesting():
    source = """
if True:
    for x in range(3):
        if x > 0:
            while x > 1:
                x -= 1
"""
    issues = NestingDepthCheck(max_depth=3).run(source)
    assert len(issues) >= 1