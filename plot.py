from numpy import *
import matplotlib.pyplot as plt

points = genfromtxt('infantmortality.csv', delimiter=',')
points = array(points[97:194])
x = []
y = []
# b = 1987.13870224
# m = -9108.58957457
# z =-3633.56106751
# a =-1071.95759342
# error = 325.382527849
# i = float(raw_input('What is the year?: '))
# x = (i/10000)
# x1 = (i/10000)
# x2 = (i/10000) ** 2
# x3 = (i/10000) ** 3
for i in range(0, len(points)):
    x.append(points[i, 1])
    y.append(points[i, 2])

plt.plot(x,y,label='Infantmortality')
plt.xlabel('Year of the statistic')
plt.ylabel('Mortality Rate')
plt.title('Infant Mortality rate of Black women in America every year')
plt.legend()
plt.show()
# print x1
# print x2
# print (a*x3 + z*x2 + m * x + b)
