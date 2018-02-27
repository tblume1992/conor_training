# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:13:16 2018

@author: t-blu
"""
import numpy as np
import matplotlib.pyplot as plt


population = np.random.randn(10000)
population = np.append(population,np.random.randn(1000)+5)



random_sample = np.random.choice(population, size=1000, replace=False)



plt.hist(population, bins = 500)
plt.show()
plt.hist(random_sample, bins = 100)
plt.show()



population_average = np.mean(population)
sample_average = np.mean(random_sample)



print(population_average)
print(sample_average)