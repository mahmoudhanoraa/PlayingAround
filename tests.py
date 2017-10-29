import calc as c

class TestSum(object):
    def test_smallNumbers(self):
        x = c.sum(2, 3)
        assert x == 5

    def test_largeNumbers(self):
        x = c.sum(500, 500)
        assert x == 1000
