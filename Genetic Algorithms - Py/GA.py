# Picobot.py

import random as r

# Dimensions of the board for the purposes of evolving Picobots
ROWS = 20
COLUMNS = 20

# Number of states in our Picobot programs
STATES = 5

# When evaluating a Picobot program for fitness, we run it TRIALS times (each time with
# a random starting location for STEPS steps.
TRIALS = 20
STEPS = 800

# The 9 possible patterns in an empty room
VALIDPATTERNS = ["xxxx", "Nxxx", "NExx", "NxWx", "xxxS", "xExS", "xxWS", "xExx", "xxWx"]

# The 4 possible directions
DIRECTIONS = ["N", "E", "W", "S"]


class Program:
    def __init__(self):
        self.rulesDict = {}

    def randomize(self):
        """ Constructs a random program """
        for i in range(STATES):
            for j in VALIDPATTERNS:
                dircop = DIRECTIONS[:]
                for n in DIRECTIONS:
                    if n in j:
                        dircop.remove(n)
                self.rulesDict[(i,j)] = (r.randrange(5), r.choice(dircop))
                #print(i, j, dircop, self.rulesDict[(i,j)])

    def getMove(self, state, pattern):
        """ Given a state and pattern string, returns a tuple of the form (newstate, move)
        indicating the move associated with that state and pattern."""
        return self.rulesDict[(state, pattern)]

    def mutate(self):
        """ Mutate the program by replacing one line of the program with another random line."""
        s = r.randrange(5)
        p = r.choice(VALIDPATTERNS)
        dircop = DIRECTIONS[:]
        for n in DIRECTIONS:
            if n in p:
                dircop.remove(n)
        self.rulesDict[(s,p)] = (r.randrange(5), r.choice(dircop))

    def crossover(self, other):
        """ Crosses self with other, returning a new program object """
        cross = r.randrange(5)
        baby = Program()
        for i in range(cross):
            for j in VALIDPATTERNS:
                baby.rulesDict[(i,j)] = self.rulesDict[(i,j)]

        for i in range(cross, 5):
            for j in VALIDPATTERNS:
                baby.rulesDict[(i,j)] = other.rulesDict[(i,j)]
        return baby


    def __repr__(self):
        output = ""
        for key in sorted(self.rulesDict.keys()):
            value = self.rulesDict[key]
            output = output + str(key[0]) + " " + str(key[1]) + " -> " + str(value[0]) + " " + str(value[1]) + "\n"
        return output

class Picobot:
    def __init__(self, picobotrow, picobotcol, program):
        self.numVisited = 1  # visited one cell so far
        if min(picobotrow, picobotcol) < 0:
            input('they are negative. ')
        self.loc = [picobotrow, picobotcol]
        self.state = 0
        self.prog = program
        self.board = [[0 for i in range(COLUMNS)] for j in range(ROWS)]
        self.count = 0

    def step(self):
        """ Take one step in accordance with the current state and program """
        #print(self.loc)
        try:
            self.board[self.loc[0]][self.loc[1]] += 1
        except IndexError:
            print(self.loc)
        if self.loc[0] == 0:
            if self.loc[1] == COLUMNS-1:
                position = VALIDPATTERNS[2] #NE
            elif self.loc[1] == 0:
                position = VALIDPATTERNS[3] #NW
            else: position = VALIDPATTERNS[1]
        elif self.loc[0] == ROWS-1:
            if self.loc[1] == 0: position = VALIDPATTERNS[6] #SW
            elif self.loc[1] == COLUMNS-1: position = VALIDPATTERNS[5] #SE
            else: position = VALIDPATTERNS[4]
        elif self.loc[1] == 0:
            position = VALIDPATTERNS[8]
        elif self.loc[1] == COLUMNS-1:
            position = VALIDPATTERNS[7]
        else: position = VALIDPATTERNS[0]
        #print(self.loc)
        #print(position)

        (state, direct) = self.prog.getMove(self.state, position)
        #print(state, direct)
        if direct == 'N': self.loc[0] -= 1
        elif direct == 'S': self.loc[0] += 1
        elif direct == 'W': self.loc[1] -= 1
        else:
            self.loc[1] += 1
        if direct in position:
            input('wrong move')
        try:
            self.count = self.board[self.loc[0]][self.loc[1]]
        except IndexError:
            print(direct)
            print(position)
            print(self.loc)
            print(self.prog.rulesDict)
            input()
        self.state = state

    def run(self, steps):
        """ Run the program for the given number of steps """
        for i in range(steps):
            self.step()
            if self.count == 1: self.numVisited += 1


    def __repr__(self):
        """ Returns a string that displays the board, Picobot's location, and dots indicating
        spots that the the Picobot has visited. """
        bored = self.board[:]
        for i in bored:
            for j,p in i:
                if j == 0:
                    i[p] = ' '
                elif j > 0:
                    i[p] = '.'
        bored[self.loc[0]][self.loc[1]] = '*'
        print('________________________________________)
        for i in bored:
            print('|' + '|'.join(bored) + '|')
            print('________________________________________)

def populate(popsize):
    popul = []
    for i in range(popsize):
        p = Program()
        p.randomize()
        popul.append(p)
    return popul

def evaluateFitness(program, trials, steps):
    av = 0
    for i in range(trials):
        x = r.randrange(COLUMNS-1)
        y = r.randrange(ROWS-1)
        pico = Picobot(y,x,program)
        pico.run(steps)
        av += (pico.numVisited)/400
    return (av/trials)



def GA(popSize, generations):
    print("Grid size being used is ", ROWS, " by ", COLUMNS)
    print("Fitness is measured using", TRIALS, "random trials and running for", STEPS, "steps")
    population = populate(popSize)
    fitness = []
    parents = []
    for i in range(generations):
        #print(len(population))
        for n in population:
            #print(n.rulesDict)
            fitness.append(evaluateFitness(n, TRIALS, STEPS))

        for j in range(21): #21c2 is 210 so we will combine them variably
            a = fitness.index(max(fitness)) #n.b. that par1 & 2 are indices
            fitness[a] = 0
            parents.append(a)

        #print(parents)
        p1 = 0
        p2 = 0
        for j in range(popSize):
            if j in [20,39,57,74,90,105,119,132,144,155,165,174,182,189,195]:
                p1 += 1
                p2 = p1
            p2 +=1
            par1 = population[parents[p1]]
            par2 = population[parents[p2]]
            population[j] = par1.crossover(par2)
            population[j].mutate()
        fitness = []
        parents = []

    for n in population:
            fitness.append(evaluateFitness(n, TRIALS, STEPS)) #n.b. that fitness values are from the last trial
    best = fitness.index(max(fitness))
    print(best, max(fitness))
    print(population[best])


###### TESTING ######

#test = Program()
#test.randomize()
#print(test.rulesDict)
#pbot = Picobot(10,10,test)
#pbot.run(200)
#print(pbot.board)
#print(test.rulesDict)
#print(test.getMove(0,"xxxx"))
GA(200,20)
