# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
#
# 10 -> 1 2 4 8

N = int(input('Input max number for degree of "2" u wish : '))
degreeNumber = 2
print('All degrees of number "2" beneath number N are : ')
print(degreeNumber)
while  degreeNumber * 2 <N :
    degreeNumber *= 2
    print(degreeNumber)
