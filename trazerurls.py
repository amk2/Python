##https://stackoverflow.com/questions/36781105/import-urllib-request-importerror-no-module-named-request

import urllib
from urllib import request


resposta = urllib.request.urlopen('http://python.org')


print(resposta)


html = resposta.read()


print(html)



