
import random
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Index should by integer and positive")
        if not isinstance(value, int) or value < 0:
            raise TypeError("Value should by integer and positive")
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([random.randint(1, 27)]*off) #we can wide this list to needed key

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Index should by integer and positive")
        del self.marks[key]


s1 = Student ("Den", [5, 5, 3, 2, 5])
print(s1.marks[2]) #here we can show element of the list with 2 position
print(s1[3])  #here we can show element of the list with 2 position via the getitem method
s1[10] = 4
del s1[2]
print(s1[3])
print(s1.marks)

