def remove_repetidos (lista):
    result_list = []
    for item in lista:
        if(item not in result_list):
            result_list.append(item)

    return sorted(result_list)

remove_repetidos([2, 4, 2, 2, 3, 3, 1])