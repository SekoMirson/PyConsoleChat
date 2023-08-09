# PyConsoleChat

## Proje Hakkında

Bu projede, iki Python arasında soket ile bağlantı kurmayı amaçlayan bir örnek bulunmaktadır.

## Başlangıç

Aşağıdaki adımları takip ederek projeyi kendi bilgisayarınızda çalıştırabilirsiniz.

1. Repoyu klonlayın: `git clone https://github.com/SekoMirson/PyConsoleChat.git`
2. Proje dizinine gidin: `cd PyConsoleChat`
3. İlk Python dosyasını çalıştırın: `python server.py`
4. İkinci Python dosyasını çalıştırın: `python client.py`

## Kullanım

Projeyi nasıl kullanabileceğinizi burada anlatabilirsiniz. Örnekler, kod parçaları ve ekran görüntüleri eklemek kullanıcıların projenizi anlamalarına yardımcı olabilir.

```python
# Örnek kod parçası
import socket
import threading
import requests
import sqlite3
import os
from colorama import init, Fore, Back, Style

# Socket oluşturma
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
