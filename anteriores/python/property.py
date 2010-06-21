class Range:

    def __init__(self, x0, x1):
        self.x0 = x0
        self.x1 = x1

    def _get_range(self):
        return self.x1 - self.x0

    def _set_range(self, number):
        self.x1 = number + self.x0

    range = property(_get_range, _set_range)


a = Range(10, 20)
print a.range
a.range = 30
print a.x0, a.x1
