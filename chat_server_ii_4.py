import asyncio

CLIENTS = {}

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    
    if addr not in CLIENTS:
        CLIENTS[addr] = {"r": reader, "w": writer}
        print(f"{addr} connecté.")
    else:
        print(f"{addr} est déjà connecté.")
        return

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                print(f"{addr} s'est déconnecté.")
                break
            
            message = data.decode()
            print(f"{addr[0]}:{addr[1]} a dit : {message}")
            
            # Envoyer le message à tous les autres clients
            for client_addr, client_conn in CLIENTS.items():
                if client_addr != addr:
                    send_message = f"{addr[0]}:{addr[1]} a dit : {message}"
                    client_conn["w"].write(send_message.encode())
                    await client_conn["w"].drain()
    finally:
        # Nettoyer après la déconnexion
        if addr in CLIENTS:
            del CLIENTS[addr]
            writer.close()
            await writer.wait_closed()
            print(f"{addr} a été retiré de CLIENTS.")

async def main():
    server = await asyncio.start_server(handle_client, '192.168.239.1', 13337)
    addr = server.sockets[0].getsockname()
    print(f'Serveur en écoute sur {addr}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
