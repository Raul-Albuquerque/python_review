import json

# write
dados = {"nome": "Ana", "idade": 24, "enderecos": ["a", "b"]}
with open("dados/dados.json", "w") as f:
    json.dump(dados, f)

# open
with open("dados/dados.json", "r") as f:
    dados_json = json.load(f)
    print(dados_json)
