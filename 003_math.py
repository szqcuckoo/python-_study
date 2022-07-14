import math

a = -1
b = -2
c = 3
'''
sqr_res = math.sqrt(b **2)
print(sqr_res)
'''

delta = b ** 2 - 4 * a * c
res = (-b + math.sqrt(delta))/(2 * a)
res2 = (-b - math.sqrt(delta))/(2 * a)
print(res)
print(res2)
