import csv

# write
with open("dados/dados.csv", "w") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nome", "idade"])
    escritor.writerow(["ana", 24])

# read
with open("dados/dados.csv", newline="") as f:
    conteudo = csv.reader(f)
    for linha in conteudo:
        print(linha)
