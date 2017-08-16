# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 02:43:29 2016

@author: AB Sanyal
"""

import numpy as np
import matplotlib.pyplot as plt
import random

#Function to test fitness of offspring
def fitness(s):
    i = 0
    k = 0
    while(i < len(s)):
        k += abs(target[i] - s[i])
        i += 1
    #k = np.sqrt(k)
    return k

#Function to mutate with a chance of 5%
def mutate(c):
    p = []
    i = 0
    while (i < len(c)):
        p.append(c[i])
        q = round(np.random.uniform(0, 1), 2)
        if (q < 0.05):
            if (c[i] == 0):
                p[i] = 1
            else:
                if (c[i] == 1):
                    p[i] = 0
        i += 1
    return p

#Create a random offspring
def create_child_random():
    i = 0
    child = []
    while (i < len(target)):
        k = np.random.randint(0, 2)
        child.append(k)
        i += 1
    return child

#Create a family of random children
def create_family_random(n):
    i = 1
    children = []
    while (i <= n):
        child = create_child_random()
        children.append(child)
        i += 1
    return children

#Cross-breed at random cross-over point
def crossover(p1, p2):
    cop = np.random.randint(1, len(target))
    child = p1[:cop] + p2[cop:]
    child = mutate(child)
    return child

#Sexually recombined offsprings
def create_recombinants(p1, p2, n):
    i = 1
    family = []
    while (i <= n):
        if (np.random.uniform(0, 1) <= 0.5):
            child = crossover(p1, p2)
        else:
            child = crossover(p2, p1)
        family.append(child)
        i += 1
    return family

#Average family fitness
def avg_fitness(family):
    i = 0
    k = 0
    while (i < len(family)):
        k += fitness(family[i])
        i += 1
    k = k/(i)
    return k

#Generate target string array
#target = [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]

#To generate a random target
target = []

i = 0
while (i < 20):
    #k = 1
    target.append(1)
    target.append(0)
    target.append(1)
    i += 1

print("Target to achieve:")
print(target)
#Create 10 random offsprings
family = create_family_random(100)

#Check the fitness of offsprings and find the best one
bestfitness = len(target)
topfitness = len(target)
counter = 1
#indexarray = []
fitnesscounter = []
avgfitnesscounter = []
while (bestfitness != 0):
    #print("Family in generation " + str(counter) + ":")
    #print(family)
    i = 0
    while (i < len(family)):
        k = fitness(family[i])
        if (k <= topfitness):
            topfitness = k
            p1 = family[i]
        i += 1
    bestfitness = fitness(p1)
    #indexarray.append(counter)
    print(":"*20 + "Generation Number " + str(counter) + ":"*20)
    fitnesscounter.append(fitness(p1))
    avgfitnesscounter.append(avg_fitness(family))
    q = np.random.randint(0, len(family))
    p2 = family[q]
    family = create_recombinants(p1, p2, 100)
    counter += 1
    print("Average fitness of this generation:")
    print(avg_fitness(family))
    print("Best offspring:")
    print(p1)
    print("Fitness of best offspring:")
    print(fitness(p1))
    #print("Selected random offspring:")
    #print(p2)
    print("Fitness of random offspring:")
    print(fitness(p2))
    print("*"*20)

print("*"*20)
print("Target matched in " + str(counter - 1) + " steps.")

plt.plot(fitnesscounter)
plt.show()
#plt.plot(avgfitnesscounter)
#plt.show()