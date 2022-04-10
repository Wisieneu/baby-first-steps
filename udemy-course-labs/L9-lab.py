import random


'''
def getcolors(colorlist, length):
    if length > len(colorlist) or type(length) != int or type(colorlist) != list:
        return None
    return colorlist[0:length]
'''



def list_combinations(input_list, length):
    result = []
    while len(result) < length:
        random_element = random.choice(input_list)
        result.append(random_element)
        print(result)
        input_list.remove(random_element)
    return result

print(list_combinations(['blue', 'red', 'yellow', 'green',], 3))
print(list_combinations(['blue', 'red', 'yellow', 'green', 'black', 'white', 'purple'], 4))
print(list_combinations(['blue', 'red', 'yellow', 'green','white', 'purple'], 3))
print(list_combinations(['blue', 'red', 'yellow', 'green'], 1))
print(list_combinations(['blue', 'red', 'yellow', 'green',], 2))

# TO BE REVIEVED