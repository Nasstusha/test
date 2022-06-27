a = [1, 2, 4, "l", 8]
def test_1(a):
    for i in a:
        assert type(i) == 'int'