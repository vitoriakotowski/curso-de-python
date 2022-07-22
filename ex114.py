import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('O site Pudim não está acessível no momento.')
else:
    print('Tudo certo, consegui acessar o site Pudim!')
    print(site.read()) # mostra o código/conteúdo html do site inteiro