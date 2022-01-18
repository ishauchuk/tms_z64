"""
Consider the implementation of composition in Python as an example. Suppose you 
want to write a program that calculates the area of wallpaper for pasting 
the room. At the same time, windows, doors, floors and ceilings do not need to 
be pasted over. Before writing the program, let's do object-oriented design. 
That is, let's figure out what is what. The room is a rectangular
parallelepiped consisting of six rectangles. Its area is the sum of the areas
of its constituent rectangles. The area of the rectangle is the product of its
length and width.

According to the condition of the problem, the wallpaper is glued only to the 
walls, therefore the areas of the upper and lower. We don't need rectangles. 
It can be seen from the figure that the area of one wall is equal to xz, 
the second - yz. Opposite rectangles are equal, so the total area of the four 
rectangles is S = 2xz +2уz = 2z(x+y).

Then from this area it will be necessary to subtract the total area of doors
and windows, since they are not pasted over. There are three types of objects:
windows, doors and rooms. It turns out three classes. Windows and doors are 
parts of the room, so let them be part of the room object. For this problem, 
only two properties are essential - length and width. Therefore the classes 
"windows" and "doors" can be combined into one. If other properties were 
important (e.g. glass thickness, door material), you should create one class 
for windows and another class for doors. As long as we get by with one and all 
we need from it is the area of the object.
"""


class WinDoor:
    def __init__(self, x, y, name="unk"):
        self.x = x
        self.y = y
        self.name = name
        self.square = x * y

    def __repr__(self):
        return f'{self.name} {self.x}x{self.y}'


class Room:
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.wd = []

    def addWD(self, w, h, name='unk'):
        self.wd.append(WinDoor(w, h, name))

    def workSurface(self):
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        return new_square


room_1 = Room(3, 3, 2.5)
print(room_1.square)

room_1.addWD(1.5, 1.5, 'big_win')
room_1.addWD(1, 2, 'fidoor')
room_1.addWD(0.20, 0.40, 'schel')

print(room_1.wd)

print(room_1.workSurface())