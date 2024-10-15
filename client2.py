import socket
import os

def send_message(client_socket):
    message = input("Entrez votre message : ")
    client_socket.send('msg'.encode('utf-8'))
    client_socket.send(message.encode('utf-8'))
    
    # Recevoir la confirmation du serveur
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Réponse du serveur : {response}")

def send_file(client_socket):
    file_path = input("Entrez le chemin du fichier : ")
    
    if os.path.exists(file_path):
        filename = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        client_socket.send('file'.encode('utf-8'))
        client_socket.send(filename.encode('utf-8'))
        client_socket.send(str(file_size).encode('utf-8'))
        
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                client_socket.send(chunk)
        
        # Recevoir la confirmation du serveur
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Réponse du serveur : {response}")
    else:
        print("Le fichier n'existe pas.")

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Se connecter au serveur
    server_ip = input("Entrez l'IP du serveur : ")
    client_socket.connect((server_ip, 12345))

    while True:
        action = input("Tapez 'msg' pour envoyer un message ou 'file' pour envoyer un fichier : ")
        
        if action == 'msg':
            send_message(client_socket)
        elif action == 'file':
            send_file(client_socket)
        else:
            print("Commande non reconnue.")

        continuer = input("Voulez-vous continuer ? (oui/non) : ")
        if continuer.lower() != 'oui':
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()
