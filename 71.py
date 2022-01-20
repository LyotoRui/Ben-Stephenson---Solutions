#Напишите программу, выводящую на экран 15 приближений числа π. 
#В первом приближении должно быть использовано только первое слага-
#емое приведенного бесконечного ряда. Каждое очередное приближение 
#должно учитывать следующее слагаемое, тем самым увеличивая точность 
#расчета.

constant = 3
even = 0
odd = 0

i_odd = list(range(4, 32, 4))
j_odd =  list(range(5, 39, 4))
k_odd = list(range(6, 46, 4))

i_even = list(range(2, 20, 4))
j_even = list(range(3, 28, 4))
k_even = list(range(4, 36, 4))


for i,j,k in zip(i_odd, j_odd, k_odd):
    odd += 4 / (i * j * k)

for i,j,k in zip(i_even, j_even, k_even):
    even += 4 / (i * j * k)


pi = constant + even - odd
print('The value of π(pi) after 15 iterations is: {}'. format(pi))
