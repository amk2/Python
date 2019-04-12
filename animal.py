import pickle
class Animal(object):
    attrs = ['nome', 'especie', 'genero', 'peso', 'altura', 'idade']
    def __init__(self, **args):
        # Crie os atributos no objeto a partir da lista
        # Os atributos tem None como valor default
        for attr in self.attrs:
            setattr(self, attr, args.get(attr, None))

    def __repr__(self):
        dic_attrs = {}
        for attr in self.attrs:
            dic_attrs[attr] = getattr(self, attr)
        return 'Animal: %s' % str(dic_attrs)

    def salvar(self):

        dic_attrs = {}
        for attr in self.attrs:
            dic_attrs[attr] = getattr(self, attr)
        pickle.dump(dic_attrs, file('a.pkl', 'w'))

    def desfazer(self):

        attrs = pickle.load(file('a.pkl'))
        for attr in attrs:
            setattr(self, attr, attrs[attr])


# Teste
gato = Animal(nome='Tinker', especie='Gato', genero='m', peso=6, altura=0.30, idade=4)
gato.salvar()
gato.idade = 5
print gato
gato.desfazer()
print gato

# Para i na lista 234, 654, 378, 798:
for i in [234, 654, 378, 798]:
    # Se o resto dividindo por 3 for igual a zero:
    if i % 3 == 0:
        # Imprime...
        print i, '/ 3 =', i / 3

