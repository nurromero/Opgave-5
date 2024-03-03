from socket import *
import threading
import random
import json

def process_request(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data: 
                break

            request = json.loads(data)
            command = request.get('method')
            number1 = request.get('Tal1')
            number2 = request.get('Tal2')

            if command not in ["Random", "Add", "Subtract"]:
                response = {"error": "Unknown command, try again."}
            else:
                if command == "Random":
                    result = random.randint(number1, number2) 
                elif command == "Add":
                    result = number1 + number2
                elif command == "Subtract":
                    result = number1 - number2

                response = {"result": result}

            response_json = json.dumps(response)
            client_socket.send(response_json.encode())
        except ValueError:
            response = {"error": "Invalid request format. Write it like this: {'method': 'Add', 'Tal1': 1, 'Tal2': 6}"}
            response_json = json.dumps(response)
            client_socket.send(response_json.encode())

    client_socket.close()

server_port = 8080
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(5)
print('Server is ready.')

while True:
    connection_socket, addr = server_socket.accept()
    threading.Thread(target=process_request, args=(connection_socket,)).start()
