url = "www.bbc.com"
partes = url.split('.')
first = partes[0]
url_nome = first[first.find('//')+2:]
if 'www' in url_nome:
    url_nome = partes[1]
print (url_nome)