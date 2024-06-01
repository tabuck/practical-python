# bounce.py
#
# Exercise 1.5

height = 100 #meters
rebound = 3/5 
numBounces = 10

for i in range(numBounces):
    height = height * rebound
    print(i, round(height,4))
