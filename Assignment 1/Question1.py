from random import uniform
import matplotlib.pyplot as plt

# Explaination
# - First calculate the CDF of the distribution given using the pdf. 
# - Calculate the inverse of this CDF and define a function for the same. 
# - generate uniform random variables and pass it as argument to difined inverse cdf function. 
# - Store the function return values in an array and plot the density

def pdf(x):
    return ( 2(1-x))

def inv_cdf(u):
    x = 1 - (1-u)**0.5 
    return x 

sim_vector = [0]*1000
for i in range(0,1000):
    u = uniform(0,1)
    sim_vector[i] = inv_cdf(u)

plt.hist(sim_vector, density=True)
plt.show()

