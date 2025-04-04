from testsuite import matching


def test_foo():
    assert {'fop': 1} == matching.PartialDict({'foo': 'bar'})
