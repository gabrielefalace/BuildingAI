# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, c):
    for f in X:
        price = 0
        for i in range(0, len(f)):
            price += c[i]*f[i]      
        print(price)

predict(X, c)


# alternative version with numpy

import numpy as np

x = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100]])
c = np.array([3000, 200 , -50, 5000, 100])

print(x @ c)
