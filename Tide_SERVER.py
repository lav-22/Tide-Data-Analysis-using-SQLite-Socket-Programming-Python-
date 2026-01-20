import socket
import sqlite3


def menu():
    return """
    1. Highest high tide with one corresponding date and time it happened
    2. Lowest low tide with one corresponding date and time it happened
    3. Largest tidal range
    4. Smallest tidal range
    """


def highest_tide():
    query = "SELECT Date, Time, Max(height) FROM Tide WHERE isHigh = 1"
    cursor = connection.execute(query)
    data = cursor.fetchall()
    return str(data[0][2])


def lowest_tide():
    query = "SELECT Date, Time, Min(height) FROM Tide WHERE isHigh = 0"
    cursor = connection.execute(query)
    data = cursor.fetchall()
    return str(data[0][2])


def largest_tidal_range():
    query = "SELECT Height FROM Tide"
    cursor = connection.execute(query)
    data = cursor.fetchall()
    data = [i[0] for i in data]
    data = max([abs(data[i] - data[i + 1]) for i in range(0, len(data) - 1)])
    return str(round(data, 2))


def smallest_tidal_range():
    query = "SELECT Height FROM Tide"
    cursor = connection.execute(query)
    data = cursor.fetchall()
    data = [i[0] for i in data]
    data = min([abs(data[i] - data[i + 1]) for i in range(0, len(data) - 1)])
    return str(round(data, 1))


connection = sqlite3.connect("tide.db")

listen_socket = socket.socket()
listen_socket.bind(("127.0.0.1", 12345))
listen_socket.listen()

new_socket, addr = listen_socket.accept()

Flag = True

while Flag:
    new_socket.sendall(menu().encode() + b"\n")
    data = b""
    while b"\n" not in data:
        data += new_socket.recv(1024)
    print("CLIENT REQUEST: " + data.decode())

    if data.decode() == "1\n":
        new_socket.sendall(highest_tide().encode() + b"\n")
    elif data.decode() == "2":
        new_socket.sendall(lowest_tide().encode() + b"\n")
    elif data.decode() == "3":
        new_socket.sendall(largest_tidal_range().encode() + b"\n")
    elif data.decode() == "4":
        new_socket.sendall(smallest_tidal_range().encode() + b"\n")
    Flag = False

connection.close()
new_socket.close()
listen_socket.close()

#%%
