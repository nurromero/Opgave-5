from socket import *
import json

def ask_user_input():
    command = input("Enter command (Random/Add/Subtract): ")
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    request = {"method": command, "Tal1": number1, "Tal2": number2}
    return json.dumps(request)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('localhost', 8080))

while True:
    try:
        user_input = ask_user_input()
        clientSocket.send(user_input.encode())
        response = clientSocket.recv(1024).decode()
        print("Server response:", response)
    except KeyboardInterrupt:
        print("Closing client...")
        break

clientSocket.close()
