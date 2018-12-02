from fixtures import avg, average, mean
functions = [avg, average, mean]


def test_aliased_functions_have_aliased_name():
    function_names = 'avg average mean'.split()
    for expected, actual in zip(function_names, map(lambda x: x.__name__, functions)):
        assert expected == actual


def test_aliased_functions_have_same_behavior():
    xs = [1, 2, 3]
    assert len({f(xs) for f in functions}) == 1
