"""
Listas
  - Ordenada
  - mutável
"""

lista = [1, "python", 2]

# acessando um valor
print(lista[0])
# output 1

# alterando um valor
lista[0] = "novo"

print(lista)

# adicionando um valor com append
lista.append(3)

print(lista)

# adicionando um valor com insert
lista.insert(0, 1)
print(lista)
