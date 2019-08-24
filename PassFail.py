
def readListOfGrades():
    gradeList = open("Prob01.in.txt", "r")
    numGrades = gradeList.readline()

    for grade in gradeList:
        determinePassFail( grade )

    gradeList.close()


def determinePassFail( grade ):
    if int(grade) >= 70:
        print("PASS")
        return()

    print("FAIL")

readListOfGrades()