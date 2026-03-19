# open()

# write
with open("dados/dados.txt", "w") as f:
    f.write("Olá mundo")

# read
with open("dados/dados.txt", "r") as f:
    content = f.read()

# append
with open("dados/dados.txt", "a") as f:
    f.write("\nnova linha")
