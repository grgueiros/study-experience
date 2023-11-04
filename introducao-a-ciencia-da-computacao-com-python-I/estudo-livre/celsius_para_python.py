while(True):
    temperatura_farenheit = input("\nDigite a temperatura em graus Farenheit: ")
    temperatura_celsius = (int(temperatura_farenheit) - 32) * 5 / 9;

    print('A temperatura em graus celsius é: ', temperatura_celsius)