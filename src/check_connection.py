import socket


def check_internet_access():
    try:
        socket.create_connection(("www.nbrb.by", 80))
        return True
    except OSError:
        return False
