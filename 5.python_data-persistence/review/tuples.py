"""
Tuplas
  - Ordenada
  - imutável
"""

t = 123, 456, "oi"
print(t)

# acessando um valor
print(t[1])

# alterando um valor
t[1] = "novo"
print(t)

# output TypeError: 'tuple' object does not support item assignment

# criando uma tupla com outra tupla
v = t, [1, 2, 3]
print(v)
