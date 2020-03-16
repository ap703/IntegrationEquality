import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quad

perc = 0.001
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

x = np.arange(startPoint, endPoint, 0.1)
y = np.vectorize(f)(x)

equalPoints = list()
equalPoints.append(equalPoint)

left_integral = integral(startPoint,equalPoint)
right_integral = integral(equalPoint,endPoint)
intPerc1 = integralPercentage(equalPoint)*100
intPerc2 = (1-integralPercentage(equalPoint))*100

while left_integral[0]/right_integral[0] <= (50-perc)/50 or left_integral[0]/right_integral[0] >= (50+perc)/50:
    if left_integral[0] > right_integral[0]:
        equalPoint = equalPoint-(((left_integral[0]/(left_integral[0]+right_integral[0]))-0.5)/(0.5)*(equalPoint-startPoint))
    else:
        equalPoint = equalPoint+(((right_integral[0]/left_integral[0]+right_integral[0])-0.5)/(0.5)*(equalPoint-endPoint))
    equalPoints.append(equalPoint)
    left_integral = integral(startPoint,equalPoint)
    right_integral = integral(equalPoint,endPoint)
    intPerc1 = integralPercentage(equalPoint)*100
    intPerc2 = (1-integralPercentage(equalPoint))*100

plt.plot(x,y)
for num,point in enumerate(equalPoints):
    xPoints = np.array([point,point])
    yPoints = np.array([0,f(point)])
    plt.plot(xPoints,yPoints,label="Iteration" + str(num+1))
    print("Value {} - {} : {}".format(point, integralPercentage(point)*100, (1-integralPercentage(point))*100))
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend()
plt.show()
