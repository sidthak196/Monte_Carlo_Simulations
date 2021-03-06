from cmath import log
from random import uniform
import matplotlib.pyplot as plt

#inverse CDF
def inv_CDF(u):
    return log(2*u)


vec = [0] * 10000
for i in range(0,10000):
    u = 0.5 * uniform(0,0.5)
    v = uniform(0,1)
    vec[i] = inv_CDF(u) * (1 if v < 0.5 else -1)

plt.hist(vec,density= True)
plt.show()



