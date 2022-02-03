import socket
import sys

sock = socket.socket()
port = int(sys.argv[1]) if len(sys.argv) >= 2 else 8800
sock.connect(("127.0.0.1", port))

if __name__ == "__main__":
    while True:
        choice_1 = input("Enter '0' to exit. \
            Press 'Enter' to continue:\n")
        if choice_1 == '0':
            break
        else:
            width = input("Enter the width of the room in meters:\n")
            sock.send(width.encode("utf-8"))

            length = input("Enter the length of the room in meters:\n")
            sock.send(length.encode("utf-8"))

            height = input("Enter the height of the room in meters:\n")
            sock.send(height.encode("utf-8"))

            choice_2 = input(
                'Enter the number of areas that do not need to be wallpapered:\n')
            sock.send(choice_2.encode("utf-8"))

            for areas in range(int(choice_2)):
                o_width = input("Enter width object:\n")
                sock.send(o_width.encode("utf-8"))

                o_height = input("Enter height object:\n")
                sock.send(o_height.encode("utf-8"))

                o_name = input("Enter object name:\n")
                sock.send(o_name.encode("utf-8"))

            wallpapers_l = input("Enter the length of the wallpaper roll:\n")
            sock.send(wallpapers_l.encode("utf-8"))

            wallpapers_w = input("Enter the width of the wallpaper roll:\n")
            sock.send(wallpapers_w.encode("utf-8"))

            room_ws = sock.recv(1024).decode("utf-8")
            square_wp = sock.recv(1024).decode("utf-8")
            print(f"Square glued surface is {room_ws} square meters.",
                  f"Number of required wallpaper rolls needed is {square_wp}.\n")
