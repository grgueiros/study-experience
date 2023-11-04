def maximo_entre_dois(x, y):
    return x if x > y else y;

def maximo(x, y, z):
    return maximo_entre_dois(z, maximo_entre_dois(x, y))