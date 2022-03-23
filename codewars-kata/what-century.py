#   -   Return the century of the input year. 
#   -   The input will always be a 4 digit string, so there is no need for validation.



def what_century(year):
    result = 0
    print(year[-2::])
    result += int(year[0:2]) + 1
    if year[-2::] == '00':
        result -= 1
    result = str(result)
    if result[-2] == '1':
        result += 'th'
    elif result[-1] == '3':
        result += 'rd' 
    elif result[-1] == '2':
        result += 'nd' 
    elif result[-1] == '1':
        result += 'st'
    else: 
        result += 'th'
    
    return result



#   -   Tests

what_century(2011)
what_century(2154)
what_century(2259)
what_century(1124)
what_century(2000)
what_century(1999)
what_century(4441)
what_century(2022)