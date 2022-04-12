def calculate_paint(efficency_ltr_per_m2, *rooms):
    result = 0
    for i in rooms: 
        result += sum(i) if type(i) != int else i
    return "You will need {} litres of farb".format((result * efficency_ltr_per_m2))

print(calculate_paint(2, 27, 31, 33))
print(calculate_paint(2, [27, 31, 33]))
rx = [27, 31, 33]
print(calculate_paint(2, *rx))