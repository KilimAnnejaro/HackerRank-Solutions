# Enter your code here. Read input from STDIN. Print output to STDOUT
# Thanks to Thomas Ulrich for his invaluable assistance.
# This code creates dictionaries for students, appending their scores by subject, then it returns the average to produce a grade for the student.
# The input is composed like this: "name mark1 mark2 mark3 ... numberofmarks"
import sys
N = int(input())
scores = []
x = sys.stdin.read()  
grades = x.split("\n")
scores.append(grades)
mathmarks = {}
physicsmarks = {}
chemistrymarks = {}
scores = scores[0]
for i in range(0,N):
    x = scores[i]
    y = x.split(" ")
    mathmarks[y[0]] = float(y[1])
    physicsmarks[y[0]] = float(y[2])
    chemistrymarks[y[0]] = float(y[3])
student = scores[N]
a = float((mathmarks[student] + chemistrymarks[student] + physicsmarks[student])/3  )
print "%.2f" % a
