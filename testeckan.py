import json
#import urllib2
from urllib.request import urlopen


url_data = urlopen('http://ver.serpro.gov.br/solr/compras_shard20_replica1/browse?&debugQuery=true&annotateBrowse=true&q=&wt=json&debugQuery=true')
#teste = eval(url_data)
json_arq = json.load(url_data)
print(json_arq)


