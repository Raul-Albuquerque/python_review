from models.carro import Carro
from models.moto import Moto


toyota = Carro("Toyota", "Toyota Corolla", 4)
Volkswagen = Carro("Volkswagen", "Volkswagen Golf", 4)
Chevrolet = Carro("Chevrolet", "Chevrolet Onix", 4)
honda = Moto("Honda", "Honda CB 500F", "esportiva")
yamaha = Moto("Yamaha", "Yamaha MT-03", "esportiva")
shineray = Moto("Shineray", "Shineray Worker 125", "casual")

print(
    f"{'Marca'.ljust(25)} | {'Modelo'.ljust(25)} | {'Status'.ljust(25)} | {'Observação:'.ljust(25)} |"
)
print(toyota)
print(Volkswagen)
print(Chevrolet)
print(honda)
print(yamaha)
print(shineray)
