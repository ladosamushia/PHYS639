# 1 - tails, 0 - heads.
import numpy.random as random
import numpy as np

Nexperiments = 10000000
outcomes = np.zeros(Nexperiments)
for i in range(Nexperiments):
    N = 1
    two_tails = False
    flip_before = random.randint(0,2)
    while two_tails == False:
        flip_current = random.randint(0,2)
        N += 1
        if flip_current == 1 and flip_before == 1:
            two_tails = True
        flip_before = flip_current
    outcomes[i] = N

print("It takes", np.mean(outcomes), "coin flips on average to get two consecutive tails")
