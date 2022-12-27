import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://ge.globo.com/")
except urllib.error.URLError:
    print("O site não está acessível no momento.")
else:
    print("Consegui acessar o site do GE com sucesso.")