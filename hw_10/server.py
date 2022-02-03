import socket
import math
import sys
from datetime import datetime


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

    def square_wallpapers(self, w_w, w_l):
        square_wallpapers = w_l * w_w
        return square_wallpapers

    def wallpapers(self, w_square):
        num_tub = self.worksurface() / w_square
        return math.ceil(num_tub)


port = int(sys.argv[1]) if len(sys.argv) >= 2 else 8800
sock = socket.socket()
sock.bind(('127.0.0.1', port))
sock.listen(1)


def curr_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


print(f"Server started at {curr_time()}.")
conn, addr = sock.accept()

if __name__ == "__main__":
    try:
        while True:

            def obj_add(*args, **kwargs):
                return room_1.add_wd(o_width, o_height, o_name)


            width = float(conn.recv(1024).decode("utf-8"))
            length = float(conn.recv(1024).decode("utf-8"))
            height = float(conn.recv(1024).decode("utf-8"))
            room_1 = Room(width, length, height)
            choice_2 = int(conn.recv(1024).decode("utf-8"))
            for areas in range(choice_2):
                o_width = float(conn.recv(1024).decode("utf-8"))
                o_height = float(conn.recv(1024).decode("utf-8"))
                o_name = conn.recv(1024).decode("utf-8")
                obj_add(o_width, o_height, o_name)
            wallpapers_l = float(conn.recv(1024).decode("utf-8"))
            wallpapers_w = float(conn.recv(1024).decode("utf-8"))
            wallpapers_square = room_1.square_wallpapers(wallpapers_l,
                                                         wallpapers_w)

            room_ws = room_1.worksurface()
            conn.send((str(room_ws)).encode("utf-8"))
            square_wp = room_1.wallpapers(wallpapers_square)
            conn.send((str(square_wp)).encode("utf-8"))

    except ValueError:
        conn.close()

    finally:
        print(f"Server stopped at {curr_time()}.")
