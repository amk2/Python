#https://medium.com/grupy-rn/trabalhando-com-python-e-mongodb-1d23ee042658
from pymongo import MongoClient
import datetime

musica = {
              "nome": "Nothing left to say",
              "banda": "Imagine Dragons",
              "categorias": ["indie", "rock"],
              "lancamento": datetime.datetime.now()
             }

#cliente = MongoClient('localhost', 27017)

cliente = MongoClient('mongodb://localhost:27017/')

banco = cliente['test-database']

album = banco['test-collection']


album = banco.album
musica_id = album.insert_one(musica).inserted_id
musica_id

