import time
class Puzzle:
    def __init__(self, level : int, puzzle : list, solusi):
        self.level = level
        self.puzzle = puzzle
        g_cost = 0
        for i in range(16):
            if(self.puzzle[i] != i+1 and self.puzzle[i] != 16):
                g_cost += 1
        self.cost = self.level + g_cost
        self.solusi = solusi    #List of Char : 'L', 'R', 'U', 'D'

    def reachable(self):
        count = 0
        for i in range(15):
            for j in range(i+1,16,1):
                if(self.puzzle[j] < self.puzzle[i]):
                    count += 1
        for i in range(15):
            if(self.puzzle[i] == 16 and i in [1,3,4,6,9,11,12,14]):
                count += 1
        if(count%2 == 0):
            return True
        else:
            return False

    def possibleMove(self):
        moveSet = ['L', 'U', 'D', 'R']
        blankPos = -1
        for i in range(16):
            if (self.puzzle[i] == 16):
                blankPos = i
                if (i%4 == 0):
                    moveSet.remove('L')
                if (i//4 == 0):
                    moveSet.remove('U')
                if (i//4 == 3):
                    moveSet.remove('D')
                if ((i+1)%4 == 0):
                    moveSet.remove('R')
        move_puzzle = {}
        for move in moveSet:
            tempPuzzle = self.puzzle[:]
            if(move == 'L'):
                tempValue = tempPuzzle[blankPos]
                tempPuzzle[blankPos] = tempPuzzle[blankPos-1]
                tempPuzzle[blankPos-1] = tempValue
            if(move == 'U'):
                tempValue = tempPuzzle[blankPos]
                tempPuzzle[blankPos] = tempPuzzle[blankPos-4]
                tempPuzzle[blankPos-4] = tempValue
            if(move == 'D'):
                tempValue = tempPuzzle[blankPos]
                tempPuzzle[blankPos] = tempPuzzle[blankPos+4]
                tempPuzzle[blankPos+4] = tempValue
            if(move == 'R'):
                tempValue = tempPuzzle[blankPos]
                tempPuzzle[blankPos] = tempPuzzle[blankPos+1]
                tempPuzzle[blankPos+1] = tempValue
            move_puzzle.update({move : tempPuzzle})
        return move_puzzle
    
    def isSolution(self):
        for i in range(16):
            if(self.puzzle[i] != i+1):
                return False
        return True

def BranchnBound(notVisited : list): #parameter berisi list of object Puzzle
    if(len(notVisited) > 0):
        visited = []
        countAccess = 0
        while(True):
            greaterLevel = notVisited[0].level
            min = notVisited[0].cost
            idxPuzzleMinCost = 0
            for i in range (len(notVisited)):
                if min > notVisited[i].cost:
                    min = notVisited[i].cost
                    greaterLevel = notVisited[i].level
                    idxPuzzleMinCost = i
                elif min == notVisited[i].cost:
                    if greaterLevel < notVisited[i].level:
                        min = notVisited[i].cost
                        greaterLevel = notVisited[i].level
                        idxPuzzleMinCost = i
            countAccess += 1
            a = 0
            for i in notVisited[idxPuzzleMinCost].puzzle:
                if i==16:
                    print(0,"\t", end="")
                else:
                    print(i,"\t", end="")
                if ((a+1)%4 == 0):
                    print()
                a += 1
            print("COST IS: ",notVisited[idxPuzzleMinCost].cost, ", LEVEL IS:", notVisited[idxPuzzleMinCost].level)
            if (notVisited[idxPuzzleMinCost].isSolution()):
                finalSolution = notVisited[idxPuzzleMinCost].solusi
                return countAccess, finalSolution
            else:
                dictPossibleMove = notVisited[idxPuzzleMinCost].possibleMove()
                for items in dictPossibleMove.items():
                    if(items[1] not in visited):
                        newLevel = notVisited[idxPuzzleMinCost].level + 1
                        newSolution = notVisited[idxPuzzleMinCost].solusi + items[0]
                        newPuzzle = Puzzle(newLevel,items[1],newSolution)
                        notVisited.append(newPuzzle)
                trashPuzzle = notVisited.pop(idxPuzzleMinCost)
                visited.append(trashPuzzle.puzzle)
