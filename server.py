import socket
import threading

def start_server(my_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", my_port))
    server_socket.listen(5)

    def handle_client(conn, addr):
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"\n{data.decode()}\n> ", end="")
            except:
                break
        conn.close()

    def accept_loop():
        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

    threading.Thread(target=accept_loop, daemon=True).start()
    print(f"Server running on port {my_port}")


def start_client(peer_ip, peer_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((peer_ip, peer_port))

    def send_messages():
        while True:
            msg = input("> ")
            client_socket.sendall(msg.encode())

    threading.Thread(target=send_messages, daemon=True).start()


if __name__ == "__main__":
    my_port = int(input("Port to listen on (e.g., 12345): ").strip())
    peer_ip = input("Peer IP: ").strip()
    peer_port = int(input("Peer port: ").strip())

    start_server(my_port)
    start_client(peer_ip, peer_port)
    threading.Event().wait()
