#Andy Carrascoza
#Midterm
#202220_SE126.02 Intermediate Prog Using Python
#Write a program in Python that reads the data stored in the “midterm.csv” file and stores its data into separates lists. Once the lists have all been populated, process the lists to display all records that have 40 or more points. Next, process the lists again to determine the average number of hits. Last, display all records, one record per line.

#Variables
#amount - Total amount of employees
#----------------------------------------------------------------------------------------------

import csv

amount = 0

first = []
last = []
phone = []
addy = []
department = []
place = []



with open("C:/2a/Lab4c.txt") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
     first.append(row[0])
     last.append(row[1])
     phone.append(row[2])
     addy.append(row[3])
     department.append(row[4])
     place.append(row[5])

     amount += 1
    
    #print("Name =", last)
    #print("Pos= ", pos)

    length = len(last)
    found = "False"
    search = input("Enter a name: ")

    for pos in range(0, length):
        #print(last[pos])
        if(search == last[pos]):
            found = "True"
            position = pos
            

    if found == "True":
        print(first[position], last[position], phone[position], addy[position], department[position], place[position])
    else:
        print("Name not on list")

    

    print("\nNumber of employees who work for the company: {0}".format(amount))