from cmath import cos, exp, log, pi, sin, sqrt
from random import randint, uniform
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

#number of simulations
# n = 10000
# hit = 0
# hit_arr = [0]*n

# for i in range(0,n):
#     hit = 0
#     for j in range(1,101):
#         x = randint(1,100)
#         if j==x:
#             hit = hit + 1
#     hit_arr[i]=hit

# print(np.mean(hit_arr))
# print(np.std(hit_arr))

# number of simulations
n = 1000000
hit = 0
hit_arr = [0]*n
cards = range(1,101)
for i in range(0,n):
    random = shuffle(cards)
    hit_arr[i] = sum(1 for i in range(0,100)  if cards[i]==random[i])

print(np.mean(hit_arr))
print(np.std(hit_arr))