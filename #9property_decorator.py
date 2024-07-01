#9. Свойства property. Декоратор @property | Объектно-ориентированное программирование Python

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property # do this metod with decorator and we can use it wia old when calling classmethod
    def old(self):
        return self.__old

    @old.setter #metod setter in decorator
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

# via this attribute old we can call set or get via old option with property decorator
#    old = property(get_old, set_old)


p = Person('Serg', 20)
#p.set_old(35)
#a = p.old
del p.old
p.old = 36 #setter uses automatically here
print(p.old, p.__dict__)
#print(p.get_old())
