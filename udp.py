import socket,argparse
MAX_SIZE_BYTES = 65535

def server(port):
    peaches = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = "127.0.0.1"
    peaches.bind((hostname,port))
    print(f"Listening at {hostname}")
    while True:
        data, client_address = peaches.recvfrom(MAX_SIZE_BYTES)
        carrot = data.decode('ascii')
        upper_case_message = carrot.upper()
        print(f"Client at {client_address} says {upper_case_message}")
        data = upper_case_message.encode("ascii")
        peaches.sendto(data,client_address)

def client(port):
    kiwi = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = input("Input lowercase sentence:")
    data = message.encode("ascii")
    kiwi.sendto(data, ('127.0.0.1', port))
    print(f"The OS assigned the address {kiwi.getsockname()} to me")
    data, address = kiwi.recvfrom(MAX_SIZE_BYTES)
    text = data.decode("ascii")
    print(f"The server {address} replied with {text}")


if __name__ == "__main__":
    funcs = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='UDP client and server')
    parser.add_argument('functions', choices=funcs, help='client or server')
    parser.add_argument('-p', metavar='PORT', type=int, default=3000,
                        help='UDP port (default 3000)')
    args = parser.parse_args()
    function = funcs[args.functions]
    function(args.p)