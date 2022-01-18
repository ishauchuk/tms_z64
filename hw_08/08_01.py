"""
The given program in 08_01_start_version.py has a number of shortcomings and 
shortcomings. Needs to be corrected and improved according to the next plan.
When calculating the surface to be glued, we do not "spoil" the self.square 
field. It remains full wall area. After all, it may be needed if the 
composition of the wd list changes, and you have to recalculate glued area.
However, the class does not provide for storing side lengths, although they may 
also be needed. For instance, if you need to change one of the values of an 
already existing object. The area of the room is always can be calculated if 
the original parameters are stored. Therefore, it is not necessary to save 
the area itself in the field. Correct the code so that Room objects have only 
four fields - width, length, height and wd. squares (full and pasteable)
should only evaluate when necessary by calling methods.

However, the class does not provide for storing side lengths, although they may 
also be needed. For instance, if you need to change one of the values of an 
already existing object. The area of the room is always can be calculated if 
the original parameters are stored. Therefore, it is not necessary to save the 
area itself in the field. Correct the code so that Room objects have only four 
fields - width, length, height and wd. squares (full and paste able) should
only evaluate when necessary by calling methods. The program calculates
the area for pasting, but does not say anything about how many rolls of
wallpaper will be required.

Add a method that takes the length and width of one roll as arguments and 
returns the number required, based on the area to be glued.
Design the program interface. Let it ask the user for data and give him the
area glued surface and the number of required rolls.
"""

import math


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
        self.x = x
        self.y = y
        self.z = z
        self.wd = []

    def square_room(self):
        square_room = 2 * self.z * (self.x + self.y)
        return square_room

    def add_wd(self, w, h, name='unk'):
        self.wd.append(WinDoor(w, h, name))

    def worksurface(self):
        new_square = self.square_room()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def wallpapers(self, w_w, w_l):
        w_square = w_l * w_w
        num_tub = self.worksurface() / w_square
        return math.ceil(num_tub)


while True:

    def obj_add():
        a = float(input("Enter width object:\n"))
        b = float(input("Enter height object:\n"))
        c = input("Enter object name:\n")
        return room_1.add_wd(a, b, c)


    choice_1 = input("Enter '0' to exit.Press 'Enter' to continue:\n")
    if choice_1 == '0':
        break
    else:
        width = float(input("Enter the width of the room in meters:\n"))
        length = float(input("Enter the lenght of the room in meters:\n"))
        height = float(input("Enter the height of the room in meters:\n"))
        room_1 = Room(width, length, height)
        choice_2 = int(input(
            'Enter the number of areas that do not need to be wallpapered:\n'))
        for areas in range(choice_2):
            obj_add()
        wallpapers_l = float(input(
            "Enter the length of the wallpaper roll:\n"))
        wallpapers_w = float(input(
            "Enter the width of the wallpaper roll:\n"))
        print(
            "Square glued surface is",
            room_1.worksurface(),
            "square meters.",
            "Number of required wallpaper rolls needed is",
            room_1.wallpapers(wallpapers_l, wallpapers_w),
            ".\n"
        )
