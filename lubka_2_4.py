'''
Нехай x_0=χ_1=1 x_2=8 x_i=sinx_(i-1) +x_(i-2) -x_(i-3)  , де i=3,4,5... . Визначити χ_n  .
'''
#
'''
x - число 
n=i - індекс int  
'''
import math as m
# введення
n = int(input('n='))
# обчислення 
x_i_1 = 8
x_i_2 = 1
x_i_3 = 1
for i in range(3, n+1):
    x_i = m.sin(x_i_1) + x_i_2 - x_i_3
    x_i_3 = x_i_2
    x_i_2 = x_i_1
    x_i_1 = x_i
# виведення
print('x_{0}={1}'.format(n, x_i))