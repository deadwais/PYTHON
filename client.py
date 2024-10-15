import socket

# Création d'un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect(('localhost', 12345))

# Envoi de données
while True:
 sms=input('')
 print(sms)
 client_socket.sendall(sms.encode('utf-8') )

# Réception de la réponse
 data = client_socket.recv(1024)
 print(f"Réponse du serveur : {data.decode('utf-8')}")
 datas = client_socket.recv(1024)
 print(f"Réponse du serveur : {datas.decode('utf-8')}")

# Fermeture du socket
 client_socket.close()


        