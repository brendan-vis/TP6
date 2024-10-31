import asyncio

async def handle_client(reader, writer):
    # Lire le message du client
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    
    # Afficher le message du client dans le terminal
    print(f"Reçu {message!r} depuis {addr}")
    
    # Envoyer la réponse au client
    response = f"Hello {addr[0]}:{addr[1]}"
    writer.write(response.encode())
    await writer.drain()
    
    # Fermer la connexion
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '', 13337)
    
    addr = server.sockets[0].getsockname()
    print(f'Service sur {addr}')

    async with server:
        await server.serve_forever()

# Lancer le serveur
if __name__ == "__main__":
    asyncio.run(main())
