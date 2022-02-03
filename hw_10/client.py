import socket
import sys

sock = socket.socket()
port = int(sys.argv[1]) if len(sys.argv) >= 2 else 8800
sock.connect(("127.0.0.1", port))


def room_parameters():
    room_params = ['width', 'length', 'height']
    for i in room_params:
        param_room = input(f"Enter the {i} of the room in meters:\n")
        sock.send(param_room.encode("utf-8"))


def areas_parameters(*args):
    for area in range(int(*args)):
        area_params = ['width', 'height', 'name']
        for i in area_params:
            param_area = input(f"Enter object {area + 1} {i}:\n")
            sock.send(param_area.encode("utf-8"))


def wallpapers_parameters():
    wallpapers_params = ['length', 'width']
    for i in wallpapers_params:
        param_wallpapers = input(f"Enter the {i} of the wallpaper roll:\n")
        sock.send(param_wallpapers.encode("utf-8"))


if __name__ == "__main__":
    while True:
        choice_1 = input("Enter '0' to exit. \
            Press 'Enter' to continue:\n")
        if choice_1 == '0':
            break
        else:
            room_parameters()

            choice_2 = input(
                'Enter the number of areas that do not need to be '
                'wallpapered:\n')
            sock.send(choice_2.encode("utf-8"))

            areas_parameters(choice_2)
            wallpapers_parameters()

            room_ws = sock.recv(1024).decode("utf-8")
            square_wp = sock.recv(1024).decode("utf-8")

            print(f"Square glued surface is {room_ws} square meters.",
                  f"Number of required wallpaper rolls needed is {square_wp}.\n")
