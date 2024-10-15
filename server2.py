import socket
import threading
import os

# Fonction pour gérer chaque client connecté
def handle_client(client_socket, address):
    print(f"Connexion acceptée de {address}")

    while True:
        try:
            # Recevoir le type de requête (message ou fichier)
            request_type = client_socket.recv(1024).decode('utf-8')
            
            if request_type == 'msg':
                message = client_socket.recv(1024).decode('utf-8')
                print(f"Message de {address}: {message}")
                client_socket.send("Message reçu".encode('utf-8'))
            
            elif request_type == 'file':
                filename = client_socket.recv(1024).decode('utf-8')
                file_size = int(client_socket.recv(1024).decode('utf-8'))
                
                with open(f'received_{filename}', 'wb') as f:
                    bytes_received = 0
                    while bytes_received < file_size:
                        chunk = client_socket.recv(1024)
                        if not chunk:
                            break
                        f.write(chunk)
                        bytes_received += len(chunk)
                        
                print(f"Fichier reçu : {filename} (taille: {file_size} octets)")
                client_socket.send("Fichier reçu".encode('utf-8'))
                
        except ConnectionResetError:
            print(f"Connexion fermée par {address}")
            break

    client_socket.close()


def start_server():
    # Créer une socket serveur TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)
    print("Serveur en attente de connexion...")

    while True:
        # Accepter les connexions entrantes
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()