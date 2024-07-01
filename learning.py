class Point:
    def __new__(cls, *args, **kwargs):
        print ("Вызов __туц__ для " + str(cls))

     def __init__(self, x=0, y=0):
         print("Вызов __init__ для " + str(self))
         self.x = x
         self.y = y