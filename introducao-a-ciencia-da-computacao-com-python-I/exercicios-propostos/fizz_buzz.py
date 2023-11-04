numero = int(input("Digite um número inteiro: "))

divisivel_por_cinco = numero % 5 == 0
divisivel_por_tres = numero % 3 == 0

print("FizzBuzz" if divisivel_por_cinco and divisivel_por_tres else numero)