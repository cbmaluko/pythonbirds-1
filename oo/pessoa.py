class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome  = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    filho1 = Pessoa(nome='Ana Laura')
    filho2 = Pessoa(nome='Bernardo')
    mathias = Pessoa(filho1, filho2, nome='Mathias')
    print(Pessoa.cumprimentar(mathias))
    print(mathias.nome)
    print(mathias.idade)

    for filho in mathias.filhos:
        print(filho.nome)
