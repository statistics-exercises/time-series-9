import matplotlib.pyplot as plt
import numpy as np

def poisson( lam, time ) :
  # Your code to generate a poisson process goes here
  
noutcomes =   ##  Variable for the number of bars in your histogram
lamd, time = 2, 5 

# Write the code to repeatedly sample the random variable here and to
# count how often each result comes up in the list called counts here.
# Notice that you will also need to ensure that the heights of all the 
# bars in your histogram sum to one.
counts = np.zeros(noutcomes)



# This part plots the data 
xlabels = noutcomes*[0]
for i in range(noutcomes) : xlabels[i] = i
plt.bar( xlabels, counts, width=0.1 )
plt.xlabel("Random variable value")
plt.ylabel("Fraction of occurances")
plt.savefig("myhistogram.png")
