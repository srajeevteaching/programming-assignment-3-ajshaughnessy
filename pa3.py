# Programmers: Aidan
# Course: CS151, Dr. Rajeev
# Date: 10/26/2021
# Programming Assignment: 3
# Program Inputs:
# Program Outputs:

# REQUIREMENTS ANALYSIS Your program will give the user the option of calculating statistics relevant to three sports.
# You must do the calculations for the following sports in your program:

# In your program, you must do some basic error checking: check if you are going to divide by zero when relevant, and
# don’t do the calculation if that’s the case; and before typecasting input to an int, check that it is only digits,
# and don’t convert to an int or do the calculation otherwise. In any case where an error is detected, output that it
# was an error, and don’t continue the calculation – you may return a zero for the result of that calculation.

# You need to code 3 different functions to calculate the scores of the 3 sports. There should not be any input or
# output inside the three functions.

# Make the main part of your program be in a "main" function. The main function never takes parameters, and does not
# return anything. The main function will call the other functions.

# PROGRAMMING REQUIREMENTS After your first part is complete and correct, it’s time to start programming and
# then testing:

# Follow good usability/HCI principles in your input and output (make it clear the type of input you are asking for)
# Follow good use of functions Remember to define functions before they are used (so if function A calls function B,
# you need to define function B first in your program) Remember to state the purpose of the program.

# to end program
import sys

# 1 - Quarterback rating in American football

# The quarterback rating determines how good a quarterback is in passing (throwing) a football. A perfect passer rating
# in the NFL is considered to be a 158.3.

# QB rating = 100 * [5(completions/attempts – 0.3) + 0.25(passing_yards/attempts-3) + 20(touchdown_passes/attempts) +
# 2.375 – (25 * interceptions/attempts)]/6
#
# Note that attempts means the number of passing attempts made, and is the same number used throughout the equation.
# Eventually, you will want to tell the user whether or not the quarterback is a perfect passer.

def quarterback_rating(comp, attempts, passing, td, inter):
    score = 100 * ((5 * ((comp/attempts) - 0.3)) + (0.25 * ((passing/attempts) - 3)) + 20 * (td/attempts) + 2.375 -
             (25 * (inter/attempts))) / 6
    if score > 158.3:
        print("Score is a perfect passing rate")
    print("Score: ", round(score, 2))

# 2 - Calculate the score for a team in a game of Quidditch as described by the International Quidditch Association
# (http://www.iqasport.com/).
#
# A goal is scored by propelling the quaffle through a hoop. The team earns 10 points per goal. If the team has caught
# the snitch, the team earns an additional 30 points (note that there is only one snitch).

def quidditch(team1, team2, snitch):
    points1 = team1 * 10
    points2 = team2 * 10
    if(snitch == 1):
        points1 += 30
    elif(snitch == 2):
        points2 += 30
    if points1 > points2:
        print("Team 1 got ", points1, " points.")
        print("Team 2 got ", points2, " points.")
        print("Team 1 wins")
    elif points1 < points2:
        print("Team 1 got ", points1, " points.")
        print("Team 2 got ", points2, " points.")
        print("Team 2 wins")
    else:
        print("Team 1 got ", points1, " points.")
        print("Team 2 got ", points2, " points.")
        print("The teams tied")


# 3 - Calculate the final score for a gymnast on any apparatus.

# Assume there are 6 scores (we’re simplifying slightly from the real world). One score is on difficulty. The other 5
# scores are on execution. All scores are between 0 and 10 (assuming the user enters integers, you do not have to check
# for they are between 0 and 10). The final score is computed by adding the difficulty score to the average of
# the execution scores.

def gymnast_score(score, execute):
    mx = max(execute)
    mn = min(execute)
    rate = score + (sum(execute)-mx-mn)/3
    print("Gymnast scored " + str(rate) + " points")

# main
def main():
    ans = input("Enter 1 for Quarterback stats, 2 for Quidditch score, 3 for Gymnastics: ")
    if int(ans) <= 3 and int(ans) >= 1:
        ans = int(ans)
    else:
        print("Invalid input")
        sys.exit()
    if ans == 1:
        comp = input("Enter completions : ")
        if int(comp) >= 0:
            comp = int(comp)
        else:
            print("Invalid input")
            sys.exit()
        passing = input("Enter passing yards : ")
        if int(passing) >= 0:
            passing = int(passing)
        else:
            print("Invalid input")
            sys.exit()
        attempts = input("Enter attempts : ")
        if int(attempts) >= 0:
            attempts = int(attempts)
        else:
            print("Invalid input")
            sys.exit()
        td = input("Enter touchdown passes : ")
        if int(td) >= 0:
            td = int(td)
        else:
            print("Invalid input")
            sys.exit()
        inter = input("Enter interceptions : ")
        if int(inter) >= 0:
            inter = int(inter)
        else:
            print("Invalid input")
            sys.exit()
        quarterback_rating(comp, attempts, passing, td, inter)

    elif ans == 2:
        team1 = input("Enter points scored by Team 1: ")
        if int(team1) >= 0:
            team1 = int(team1)
        else:
            print("Invalid input")
            sys.exit()
        team2 = input("Enter points scored by Team 2: ")
        if int(team2) >= 0:
            team2 = int(team2)
        else:
            print("Invalid input")
            sys.exit()
        snitch = input("Enter 1 if Team 1 caught the snitch or 2 for Team 2: ")
        if int(snitch) <= 2 and int(snitch) >= 0:
            snitch = int(snitch)
        else:
            print("Invalid input")
            sys.exit()
        quidditch(team1, team2, snitch)

    elif ans == 3:
        score = input("Enter difficulty score : ")
        if score.isdigit() and int(score) >= 0:
            score = int(score)
        else:
            print("Invalid input")
            sys.exit()
        execute = []
        for i in range(5):
            temp = input("Enter execution score " + str(i + 1) + " : ")
            if temp.isdigit() and int(temp) >= 0:
                execute.append(int(temp))
            else:
                print("Invalid input")
                sys.exit()
        gymnast_score(score, execute)
    else:
        print("Invalid input")


main()