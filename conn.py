import socket


server_ip = '0.0.0.0'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.bind((server_ip, server_port))
client_socket.listen(5)

print(f'Server listening on {server_ip}:{server_port}')

try:
    while True:
        conn, addr = client_socket.accept()
        print(f"Connected client: {addr}")

        data = conn.recv(1024)
        if not data:
            print("Client disconnected")
            conn.close()
            continue

        print(f"Received: {data.decode()}")
        
        conn.close()
except KeyboardInterrupt:
    print("Server stopped by user")

finally:
    client_socket.close()
    print('Socket closed')
