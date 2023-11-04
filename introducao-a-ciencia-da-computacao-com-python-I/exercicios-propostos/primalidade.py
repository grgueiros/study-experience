entrada = int(input("Digite o valor de n: "))

i = 10
resultado = "primo"
while(i > 1):
    if entrada % i == 0 and entrada != i:
        resultado = "não primo" 
    i -= 1;

print(resultado)