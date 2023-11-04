import re

def vogal(letra):
    return True if re.search("[aAeEiIoOuU]{1}", letra) else False