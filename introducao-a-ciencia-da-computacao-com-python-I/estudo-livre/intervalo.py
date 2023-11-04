nota = input('Digite uma nota:')

pertence_ao_intervalo = 3 <= int(nota) <= 5

result = 'Sua nota não pertence ao intervalo'

if pertence_ao_intervalo:
    result = 'Sua nota pertence ao intervalo'

print(result)