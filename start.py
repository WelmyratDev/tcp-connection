import socket


while True:
    try:
        server_ip = input("PC IP address: ")
        send_message = input('Send message>>: ')
        server_port = 12345

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.connect((server_ip, server_port))

        client_socket.sendall(send_message.encode())
        print("Message Sent")

        exit = input("Continue (yes/no): ")
        if exit == 'yes':    
            continue
        else:
            client_socket.close()
            break
    except Exception as e:
        print(str(e))
        continue
    