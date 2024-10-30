import aiohttp
import aiofiles
import asyncio
import sys


async def get_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # resp = await resp.text()
            # print(resp)
            return await resp.text()



async def write_content(content, file):
    async with aiofiles.open(file, "w", encoding="utf-8") as out:
        await out.write(content)
        await out.close()



async def main():
    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <URL>")
        sys.exit(1)

    url = sys.argv[-1]
    try:
        content = await get_content(url)
        await write_content(content, "./tmp/web_page")
        print("Le contenu de la page a été sauvegardé dans /tmp/web_page.")
    except Exception as e:
        print(f"Erreur : {e}")
        
if __name__ == "__main__":
    asyncio.run(main())
