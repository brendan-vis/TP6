import sys
import requests

def get_content(url):
    response = requests.get(url)
    return response.text


def write_content(content, file):
    f = open(file, "w", encoding="utf-8")
    f.write(content)
    f.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <URL>")
        sys.exit(1)

    url = sys.argv[-1]
    try:
        content = get_content(url)
        write_content(content, "./tmp/web_page")
        print("Le contenu de la page a été sauvegardé dans /tmp/web_page.")
    except Exception as e:
        print(f"Erreur : {e}")