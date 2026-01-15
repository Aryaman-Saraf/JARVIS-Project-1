import requests
import socket

#This Function is Used to Check if the device if connected to the internet or not
def internet_available():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        try:
            requests.get("https://www.google.com", timeout=2)
            return True
        except requests.ConnectionError:
            return False