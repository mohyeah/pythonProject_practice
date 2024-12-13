class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy)**0.5

    def __str__(self):
        return f'({self.x}, {self.y})'

p1 = Point(3, 5)
p2 = Point(6, 9)
print(p1)
print(p2)
print(p1.distance_to(p2))