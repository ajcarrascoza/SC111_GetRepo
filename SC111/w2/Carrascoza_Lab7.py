#Andy Carrascoza
#Lab6A
#
#202220_SE126.02 Intermediate Prog Using Python

#------------------------------------------

import csv

first = []
last = []
department = []
position = []
salary = []





with open("C:/2a/Lab7.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
     first.append(row[0])
     last.append(row[1])
     department.append(row[2])
     position.append(row[3])
     salary.append(row[4])
     salaryAvg = int(row[4])

    

def swap(list, x):
    temp = list[x]
    list[x] = list[x + 1]
    list[x + 1] = temp
def mySortHighest(list1, list2, list3):
    length = len(list1)
    for i in range(0, length):
        for j in range(0, length - 1):
            if (list1[j] < list1[j + 1]):
                swap(list1, j)
                swap(list2, j)
                swap(list3, j)
def mySortLowest(list1, list2, list3):
    length = len(list1)
    for i in range(0, length):
        for j in range(0, length - 1):
            if (list1[j] > list1[j + 1]):
                swap(list1, j)
                swap(list2, j)
                swap(list3, j)

def totalAverage():
    length = len(department)
    found = "False"
    search = "MIS"

    for pos in range(0, length):
        if(search == department[pos]):
            found = "True"
            amount = 0 
            total = 0
            average = 0
             
            
            
        if found == "True":
            amount += 1
            total += salary
            average = total
            average /= amount

    print(salaryAvg) 
    print("\nAverage Salary of workers in the MIS department: ${0:.2f}".format(amount))


def payRise():
    length = len(salary)
    found = "False"
    

    for pos in range(0, length):
        if(salary[pos]):
            found = "True"
            amount = 0 
            
            
        if found == "True":
            amount = amount + salaryAvg
            amount = amount * 0.05
            print(amount)

        
#------------Main Program----------
    

mySortHighest(salary, last, department)
print("\n\nSorted list by Highest Annual Salary")
length = len(salary)
for i in range(0, length):
    print(last[i], "  ", department[i], " ", salary[i])

totalAverage() 

mySortLowest(salary, last, department)
print("\nSorted list by Lowest Annual Salary")
length = len(salary)
for i in range(0, length):
    print(last[i], "  ", department[i], " ", salary[i])


   
payRise()

