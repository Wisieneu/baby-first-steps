# every possible route in there polish cities, with counter


ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

gen =  ((a,b) for a in ports for b in ports if ports.index(a) < ports.index(b))
counter = 0 

try:
    for (a, b) in gen:
        counter += 1
        print("from {} to {}, route no. {}".format(a, b, counter))
        
except StopIteration:
    print('end')