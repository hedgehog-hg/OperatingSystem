def reachNextLevel(experience,threshold,reward):
    return experience + reward >= threshold

print(reachNextLevel(10,15,5))