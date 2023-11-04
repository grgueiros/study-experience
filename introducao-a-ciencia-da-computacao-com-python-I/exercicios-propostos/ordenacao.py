a = int(input("Digite um número inteiro: "))
b = int(input("Digite um número inteiro: "))
c = int(input("Digite um número inteiro: "))

eh_crescescente = b > a and c > b

print("crescente" if eh_crescescente else "não está em ordem crescente")
