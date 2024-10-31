import sys
import requests
import time

def get_content(url):
    return url


def write_content(content, file):
    f = open(file, "a", encoding="utf-8")
    f.write(content)
    f.close()

if __name__ == "__main__":
    start = time.time()
    for i in range(10000):
        i**i
    if len(sys.argv) < 2:
        print("Usage: python web_sync.py <URL>")
        sys.exit(1)

    url = sys.argv[-1]
    try:
        content = get_content(url)
        s_url = url.replace("https://", "")
        print(s_url)
        write_content(content+'\n', f"./tmp/web_{s_url}")
        print("Le contenu de la page a été sauvegardé dans /tmp/web_page.")
    except Exception as e:
        print(f"Erreur : {e}")
print(time.time() - start)
