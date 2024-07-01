# __private_method_or_argument_or_variable
# _protected_method
# public_method


class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

#create classmethod for checking value for corrected data and use this for
# value checking in other methods
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Should be numbers")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
# print(pt.get_coord())
# print(dir(pt))
# print(pt._Point__x)
# with accessify module you can additionally protect your methods or data inside class
