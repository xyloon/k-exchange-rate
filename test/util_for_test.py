def assert_equal(target, answer):
    assert check_equal_all(target, answer)


def check_equal_all(target, answer):
    if isinstance(target, tuple ) or isinstance(target, list ):
        return all([check_equal_all(a, b) for a, b in zip(target, answer)])
    elif isinstance(target, dict ):
        return all([check_equal_all(a, b) for a, b in zip(sorted(target.items()), sorted(answer.items()))])
    else:
        return target == answer


def assertIsNone(a):
    assert a is None


def assertDictEqual(a,b):
    assert_equal(
        sorted(a.items()),
        sorted(b.items())
    )