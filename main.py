import random
import math
import matplotlib.pyplot as plt
import copy
import numpy

N = 50
P = 50
G = 500
MUTRATE = 1


class individual:
    def __init__(self):
        self.gene = [0] * N
        self.fitness = 0


population = []
offspring = []


def createPopulation(thePopulation):
    for x in range(0, P):
        tempgene = []
        for x in range(0, N):
            tempgene.append(random.randint(0, 1))
        newind = individual()
        newind.gene = tempgene.copy()
        thePopulation.append(newind)
    return thePopulation


def test_function(ind):
    utility = 0
    for i in range(N):
        utility = utility + ind.gene[i]

    # print(str(utility))
    return utility


# update each individuals fitness based on current individuals status
def update_fitness(thePopulation):  # max
    best = 0
    average = 0
    for i in range(P):
        thePopulation[i].fitness = test_function(thePopulation[i])
        average += thePopulation[i].fitness
        if (best < thePopulation[i].fitness):
            best = thePopulation[i].fitness
    average = average / P
    print(average)
    # print("sum fitness = " + str(average) + ",average fitness =" + str(average / P))
    # print("Best fitness: " + str(best))
    return average, best


"""
#def update_average(pop):
    for i in range(P):
        average = numpy.mean(population[i].fitness)
    return average

#def update_best(pop):
    for i in range(P):
        average = numpy.max(population[i].fitness)
    return average
"""


# calling the function
# average_fitness = update_fitness()

# for q in range (P):

# print (population[q].fitness)

def selection(thePopulation):
    newPop = []
    print(thePopulation[1].fitness)
    for i in range(0, P):
        off1 = thePopulation[random.randint(0, P - 1)]
        off2 = thePopulation[random.randint(0, P - 1)]
        off3 = thePopulation[random.randint(0, P - 1)]
        if off1.fitness > off2.fitness and off3.fitness > off1.fitness:
            newPop.append(off1)
        elif off2.fitness > off3.fitness:
            newPop.append(off2)
        else:
            newPop.append(off3)
    return newPop


def crossover(thePopulation):
    toff1 = individual()
    toff2 = individual()
    temp = individual()
    for i in range(0, P, 2):
        toff1 = copy.deepcopy(thePopulation[i])
        toff2 = copy.deepcopy(thePopulation[i + 1])
        temp = copy.deepcopy(thePopulation[i])
        crosspoint = random.randint(0, N)
        for j in range(crosspoint, N):
            toff1.gene[j] = toff2.gene[j]
            toff2.gene[j] = temp.gene[j]
        thePopulation[i] = copy.deepcopy(toff1)
        thePopulation[i + 1] = copy.deepcopy(toff2)
    return thePopulation


def mutation(thePopulation):
    newpop = []
    for i in range(0, P):
        for j in range(0, N):
            gene = thePopulation[i].gene[j]
            mutprob = random.randint(0, 100)
            if mutprob < MUTRATE:
                if (gene == 1):
                    gene = 0
                else:
                    gene = 1
            thePopulation[i].gene[j] = gene


def generateGeneration(generationCounter, theoffspring):
    for i in range(generationCounter):
        # print("this loop: " + str(i))
        theoffspring = selection(theoffspring)
        update_fitness(theoffspring)
        theoffspring = crossover(theoffspring)
        mutation(theoffspring)
        avg, best = update_fitness(theoffspring)
        stats.append(avg)
        statsTwo.append(best)
        theoffspring = copy.deepcopy(theoffspring)


# append new individual or overwrite offspring
stats = []
statsTwo = []

population = createPopulation(population)
update_fitness(population)
offspring = crossover(population)
update_fitness(offspring)
generateGeneration(G, copy.deepcopy(offspring))

print('11.11.2021')
plt.plot(stats)
plt.plot(statsTwo)
plt.show()

# currently this is a mix between ws2 and ws3
# need a mutation function that works on floating point
# start with a maximising fitness function
#if __name__ == '__main__':
#    print_hi('PyCharm')

