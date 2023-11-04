year = int(input('Digite um ano para descobrir se ele é bissexto: '))

is_multiple_of_one_hundred = year % 100 == 0

is_multiple_of_four_hundred = year % 400 == 0

is_multiple_of_four = year % 4 == 0

is_leap_year = is_multiple_of_four and not is_multiple_of_one_hundred and not is_multiple_of_four_hundred

result = "O ano escolhido não é bissexto"

if is_leap_year:
    result = "O ano escolhido é bissexto"

print(result)