def fizzbuzz (numero):
    eh_divisivel_por_cinco = numero % 5 == 0
    eh_divisivel_por_tres = numero % 3 == 0

    if(eh_divisivel_por_cinco and eh_divisivel_por_tres):
        return 'FizzBuzz'
    
    if(eh_divisivel_por_cinco):
        return 'Buzz'
    
    if(eh_divisivel_por_tres):
        return 'Fizz'
    
    return numero