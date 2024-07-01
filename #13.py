class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self): #uses for displaying info for developer
        return f"{self.__class__}: {self.name}"

    def __str__(self):  #uses for displaying info for user
        return f"{self.name}"

class Point:
    def __init__(self, *args):
        self.__coords = args

    def returning(self):
        return self.__coords

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, 2, -5)
print(p.returning())
print(len(p))
print(abs(p))


