import matplotlib.pyplot as plt

def gradient_descent(x, y, num_iterations=1000, learning_rate=0.0001):
    coefficients = []
    a = 0
    b = 0
    for i in range(num_iterations):
        for i in range(len(x)):
            error = (a + b * x[i]) - y[i]
            a = a - error * learning_rate
            b = b - x[i] * error * learning_rate
    coefficients.append(a)
    coefficients.append(b)
    return coefficients

with open('data_iris.csv', 'r') as file:
    lines = file.readlines()
    lengte = []
    breedte = []
    for i in lines:
        l = i.split(',')
        lengte.append(float(l[0]))
        breedte.append(float(l[1]))

a, b = gradient_descent(lengte, breedte)
prediction = [a + b * x for x in lengte]
plt.scatter(lengte, breedte)
plt.plot(lengte, prediction)
plt.show()
