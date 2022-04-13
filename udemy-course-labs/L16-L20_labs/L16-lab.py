import math
import time


formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range (1000000):
    argument_list.append(i/10)

print(' NO OPTIMALIZATION '.center(60, '#'))

for formula in formulas_list:
    print(' NEXT FORMULA '.center(60, '-'))
    print('Current formula: {}'.format(formula))
    start = time.time()
    results_list = []
    for x in argument_list:
        results_list.append(eval(formula))
    print('Lowest value: {} Highest value: {}'.format(min(results_list), max(results_list)))
    stop = time.time()
    print('Task has been executed, it took %.1f seconds to perform' % (stop - start))
    

print()
print(' WITH OPTIMALIZATION '.center(60, '#'))


for formula in formulas_list:
    print(' NEXT FORMULA '.center(60, '-'))
    print('Current formula: {}'.format(formula))
    start = time.time()
    results_list = []
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    results_list.sort()
    print('Lowest value: {} Highest value: {}'. format(results_list[0], results_list[-1]))
    stop = time.time()
    print('Task has been executed, it took %.1f seconds to perform' % (stop - start))