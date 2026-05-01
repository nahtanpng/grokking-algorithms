from collections import deque

grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

fila_de_pesquisa = deque()
fila_de_pesquisa += grafo["voce"]
verificadas = []


def pessoa_e_vendedor(pessoa):
    return pessoa[-1] == "m"


while fila_de_pesquisa:
    pessoa = fila_de_pesquisa.popleft()
    if pessoa not in verificadas:
        if pessoa_e_vendedor(pessoa):
            print(pessoa + " é um vendedor de manga!")
            break
        else:
            fila_de_pesquisa += grafo[pessoa]
            verificadas.append(pessoa)
