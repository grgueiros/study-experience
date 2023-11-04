import math

x1 = float(input("Digite um número inteiro: "))
y1 = float(input("Digite um número inteiro: "))
x2 = float(input("Digite um número inteiro: "))
y2 = float(input("Digite um número inteiro: "))



distancia = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

print("longe" if distancia >= 10 else "perto")