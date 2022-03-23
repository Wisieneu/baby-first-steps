def get_middle(s):
    print(s)
    l = len(s)
    print(l)
    if l % 2 == 1 :
        m = int((l-1)/2)
        mid = s[m]
        return mid
    
    elif l % 2 == 0 :
        m = int(l/2)
        mid = s[m-1]+s[m]
        return mid


#   -   Tests

get_middle('kmhgjhf')
get_middle('kdhgfhfghfghdhf')
get_middle('kdfhdfghfghfghhf')
get_middle('ksjhdhf')
get_middle('ksfdh556y56h')
get_middle('ksdh4t45yh5b5ytnbdhf')
