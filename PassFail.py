#!/opt/local/bin/python

#This function reads in the grades from a fil
def readListOfGrades():
    gradeList = open("Prob01.in.txt", "r")
    numGrades = gradeList.readline()

    for grade in gradeList:
        determinePassFail( grade )

    gradeList.close()

#This Function determines if a grade passes or fails and print to the screen
def determinePassFail( grade ):
    if int(grade) >= 70:
        print("PASS")
        return()

    print("FAIL")

#how we run the program
readListOfGrades()