import numpy as np
import matplotlib.pyplot as plt

Hmwrk = np.array([10, 10, 8, 9.5, 3, 9, 0, 6])
Midterm = np.array([10, 10, 10, 10, 8, 5, 10, 7])
FinProj = np.array([9, 10, 10, 6, 10, 6, 8, 9])

finalGrade = np.array(4.*Hmwrk + 2.*Midterm + 4.*FinProj)

x = 0
while(x < 7):
    x = x + 1
    print finalGrade[x]

n = 0
m = 0
g = 0
while(n < 7):
    n = n + 1
    if finalGrade[n] < 60:
        m = m +1
        print "Number of students failed: ", m, "Grade: ", finalGrade[n]
    if finalGrade[n] > 95:
        g = g + 1
        print "Number of outstanding students: ",g,"/",x + 1

plt.hist(finalGrade)
plt.title("Final Grades")
plt.xlabel("Student")
plt.ylabel("Finale Grade")
plt.show()

plt.savefig('finalGrade.png')
