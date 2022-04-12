import math
argument_list = []
for i in range(0, 100):
    argument_list.append(i/10)

formula = input('wprowadz wzor zawierajacy zmienna x : ')
try:
    for i in argument_list:
        output = formula.replace('x', str(i))
        print('for argument: {} the function takes value: {}'.format(i, eval(output)))
except:
    print('invalid formula, cannot execute')