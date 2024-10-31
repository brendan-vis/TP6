import asyncio

async def handle_client(reader, writer):
    while True:
        # Lire le message du client
        data = await reader.read(1024)
        message = data.decode()
        addr = writer.get_extra_info('peername')
        
        # Afficher le message du client dans le terminal
        print(f"Message received from {addr[0]}:{addr[1]} : {message}")
        # print(f"Reçu {message!r} depuis {addr}")
        
        # Envoyer la réponse au client

        # response = f"Message received from {addr[0]}:{addr[1]} : {message}"
        response = f"Reçue"
        writer.write(response.encode())
        await writer.drain()


async def main():
    server = await asyncio.start_server(handle_client, '192.168.239.1', 13337)

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())