# I. Faire joujou avec l'asynchrone

## 1. Premiers pas

🌞 sleep_and_print.py

[sleep_and_print](./sleep_and_print.py)

```

```

🌞 sleep_and_print_async.py

[sleep_and_print_async](./sleep_and_print_async.py)

```

```

## 2. Web Requests

🌞 web_sync.py

[web_sync.py](./web_sync.py)

```

```

🌞 web_async.py

[web_async.py](./web_async.py)

```

```


🌞 web_sync_multiple.py

[web_sync_multiple.py](./web_sync_multiple.py)
```

```


🌞 web_async_multiple.py

[web_async_multiple.py](./web_async_multiple.py)
```

```

🌞 Mesure !

```
async :

python .\web_async_multiple.py https://www.ynov.com https://www.example.com https://www.wikipedia.org https://www.github.com https://www.python.org https://www.stackoverflow.com https://www.reddit.com https://www.news.ycombinator.com https://www.medium.com https://www.openai.com

Le contenu de la page a été sauvegardé dans /tmp/web_page.
3.3509602546691895


sync :

python .\web_sync_multiple.py https://www.ynov.com https://www.example.com https://www.wikipedia.org https://www.github.com https://www.python.org https://www.stackoverflow.com https://www.reddit.com https://www.news.ycombinator.com https://www.medium.com https://www.openai.com 
www.openai.com
Le contenu de la page a été sauvegardé dans /tmp/web_page.
3.270852565765381
```


# II. Chat room

## 1. Intro

## 2. Première version

🌞 chat_server_ii_2.py

[chat_server_ii_2.py](./chat_server_ii_2.py)

```

```

🌞 chat_client_ii_2.py

[chat_client_ii_2.py](./chat_client_ii_2.py)

```

```

## 3. Client asynchrone

🌞 chat_client_ii_3.py

[chat_client_ii_3.py](./chat_client_ii_3.py)

```

```

🌞 chat_server_ii_3.py

[chat_server_ii_3.py](./chat_server_ii_3.py)

```

```