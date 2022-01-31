from cmath import cos, exp, log, pi, sin, sqrt
from random import uniform
from timeit import timeit
import matplotlib.pyplot as plt

# Box Muller
def Box_Muller(n):

    norm_vals = [0]*n
    for i in range(0,int(n/2),2):
        u1 = uniform(0,1)
        u2 = uniform(0,1)
        norm_vals[i]= cos(2*pi*u2) * sqrt(-2*log(u1))
        norm_vals[i+1] = sin(2*pi*u2) * sqrt(-2*log(u1))
    plt.hist(norm_vals, density=True)

def Marsaglia_Bray(n):

    norm_vals = [0]*n
    for i in range(0,int(n/2),2):
        v1 = uniform(0,1)
        u1 = uniform(0,1) * -1 if v1 <0.5 else 1
        v2 = uniform(0,1)
        u2 = uniform(0,1)* -1 if v2 <0.5 else 1
        s = u1 + u2
        if s < 1:
            norm_vals[i] = u1 * sqrt (-2 * log(s)/s)
            norm_vals[i+1] = u2 * sqrt (-2 * log(s)/s)
    plt.hist(norm_vals, density=True)

def rational_exp(n):
    a0 = 2.50662823884
    a1 = -18.61500062529
    a2 = 41.39119773534
    a3 = -25.44106049637

    b0 = -8.47351093090
    b1 = 23.08336743743
    b2 = -21.06224101826
    b3 = 3.13082909833

    c0 = 0.3374754822726147
    c1 = 0.9761690190917186
    c2 = 0.1607979714918209
    c3 = 0.0276438810333863
    c4 = 0.0038405729373609
    c5 = 0.0003951896511919
    c6 = 0.0000321767881768
    c7 = 0.0000002888167364
    c8 = 0.0000003960315187
    norm_vals = [0]*n

    for i in range(0,n):
        u = uniform(0,1)
        y = u - 0.5 
        if max(0,y)<0.42:
            r = y*y
            norm_vals[i] = y * (((a3*r+a2)*r+a1)*r+a0)/((((b3*r+b2)*r+b1)*r+b0)*r+1)
        else:
            r= 1-u
            r = log(-log(r))
            norm_vals[i] = c0+r*(c1+r*(c2+r*(c3+r*(c4+r*(c5+r*(c6+r*(c7+r*c8)))))))
            if y< 0 :
                norm_vals[i] = - norm_vals[i]
    plt.hist(norm_vals, density=True)

def Acc_Rej(n):
    # Assuming the simpler function, g(x) as an exponention distribution with parameter 1.
    # so we calculate the ratio f(x)/g(x) and maximize it to calcuate the value at the value. This is set to be c (the multiplication constant)
    # C = squareroot of (2e / pi)
    # Now simulate 2 uniform random variables and as per the algorithm.
    c = sqrt(2*exp(1)/pi)
    norm_vals = [0]*n
    
    for i in range(0,n):
        flag = 0
        while flag == 0:
            # simulating exponential distribution - exp(1) and a uniform distribution
            # for Exponential we use the inverve method
            # invesrse for exponential => x = -log(1-u)/1
            u1 = uniform(0,1)
            y = -log(1-u1)

            # calculate f(y). Here we use (twice) the postive side of normal distribution to have the same domain as the exponential distribution.
            fy = exp(-(y.real**2)/2)*sqrt(2/pi)
            #calculate g(y) 
            gy = exp(-y.real) 

            # simulate uniform to decide if within the normal distribution.
            u2 = uniform(0,1)
            temp = fy/(c*gy)
            if u2 <= temp.real:
                norm_vals[i] = y
                flag = 1
                u3 = uniform(0,1)
                # use symetry to assign postive and negative values. 
                norm_vals[i] = norm_vals[i] * 1 if u3 <0.5 else -1
    plt.hist(norm_vals, density=True)



# Box_Muller(1000)
# Marsaglia_Bray(1000)
# rational_exp(1000)
Acc_Rej(100000)

plt.show()

# BoxMuller_time = timeit("Box_Muller(1000)",setup="from __main__ import Box_Muller", number = 100)
# Marsaglia_time = timeit("Marsaglia_Bray(1000)",setup="from __main__ import Marsaglia_Bray", number = 100)
# Rational_time = timeit("rational_exp(1000)",setup="from __main__ import rational_exp", number = 100)

# print(BoxMuller_time)
# print(Marsaglia_time)
# print(Rational_time)

#plt.hist(norm_vals, density=True)
#plt.show()
