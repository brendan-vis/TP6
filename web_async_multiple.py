import sys
import requests
import aiofiles
import asyncio

async def get_content(url):
    return url


async def write_content(content, file):
     async with aiofiles.open(file, "a", encoding="utf-8") as out:
        await out.write(content)
        await out.close()


async def main ():
    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python web_sync.py <URL>")
            sys.exit(1)

        url = sys.argv[-1]
        try:
            content = await get_content(url)
            s_url = url.replace("https://", "")
            await write_content(content+'\n', f"./tmp/web_{s_url}")
            print("Le contenu de la page a été sauvegardé dans /tmp/web_page.")
        except Exception as e:
            print(f"Erreur : {e}")
if __name__ == "__main__":
    asyncio.run(main())