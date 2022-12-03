
# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors
# Rock = 1, Paper = 2, Scissors = 3
# Loss = 0, Draw = 3, Win = 6

# Winning combinations: [C,X], [B,Z], [A,Y]
# Draw conditions: [A,X], [B,Y], [C,Z]
# Loss is anything else 

f = open("2-input.txt", "r")

totalScore = 0
# winConditions = [['C','X'], ['B','Z'], ['A', 'Y']]
# drawConditions = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]

moveToWin = {
    'A' : 'P',
    'B' : 'S',
    'C' : 'R'
}

moveToDraw = {
    'A' : 'R',
    'B' : 'P',
    'C' : 'S'
}

moveToLose = {
    'A' : 'S',
    'B' : 'R',
    'C' : 'P'
}

moveScoring = {
    'R': 1,
    'P': 2,
    'S': 3
}

for line in f:
    moves = line.split()

    moveScore = 0
    resultScore = 0
    myMove = ''

    match moves[1]:
        case 'X':
            # I should lose
            myMove = moveToLose[moves[0]]
            resultScore = 0
        case 'Y':
            # I should draw
            myMove = moveToDraw[moves[0]]
            resultScore = 3
        case 'Z':
            # I should win
            myMove = moveToWin[moves[0]]
            resultScore = 6
        case _:
            print("I definitely shouldn't be here")

    moveScore = moveScoring[myMove]

    # moveScore = moveScoring[moves[1]]

    # for condition in winConditions:
    #     if moves == condition:
    #         # we won!
    #         resultScore = 6
    #         resolved = True
    #         break
    
    # if not resolved:
    #     for condition in drawConditions:
    #         if moves == condition:
    #             # we drew!
    #             resultScore = 3
    #             resolved = True
    #             break
    
    roundScore = moveScore + resultScore
    totalScore += roundScore


print(totalScore)