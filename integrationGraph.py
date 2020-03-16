import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quad
import operator

perc = 0
startPoint = -1.5
endPoint = 3
equalPoint = (startPoint+endPoint)/2

def f(x):
    return x**3 - x**2 - 3*x + 4

integral = lambda a,b : quad(f,a,b)

def integralPercentage(point):
    int1 = integral(startPoint,point)
    int2 = integral(point,endPoint)
    return (int1[0]/(int1[0]+int2[0]))

def minMaxPoint():
    minimum = min(equalPoints)
    maximum = max(equalPoints)
    for point in equalPoints[:-1]:
        if (point < equalPoints[-1]) and (point > minimum):
            minimum = point
        elif (point > equalPoints[-1]) and (point < maximum):
            maximum = point
    return minimum,maximum

x = np.arange(startPoint, endPoint+0.1, 0.1)
y = np.vectorize(f)(x)

equalPoints = list()
equalPoints.extend([startPoint,endPoint,equalPoint])

left_integral = integral(startPoint,equalPoint)
right_integral = integral(equalPoint,endPoint)
intPerc1 = integralPercentage(equalPoint)*100
intPerc2 = (1-integralPercentage(equalPoint))*100

while left_integral[0]/right_integral[0] <= (50-perc)/50 or left_integral[0]/right_integral[0] >= (50+perc)/50:
    if left_integral[0] > right_integral[0]:
        equalPoint = (minMaxPoint()[0]+equalPoint)/2
    else:
        equalPoint = (equalPoint+minMaxPoint()[1])/2
    equalPoints.append(equalPoint)
    left_integral = integral(startPoint,equalPoint)
    right_integral = integral(equalPoint,endPoint)
    intPerc1 = integralPercentage(equalPoint)*100
    intPerc2 = (1-integralPercentage(equalPoint))*100
    print(equalPoint)

plt.plot(x,y)
for index in [0,1,-1]:
    xPoints = np.array([equalPoints[index],equalPoints[index]])
    yPoints = np.array([0,f(equalPoints[index])])
    plt.plot(xPoints,yPoints)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()

print(equalPoints[-1])
