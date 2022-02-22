#Andy Carrascoza
#Lab5A
#202220_SE126.02 Intermediate Prog Using Python
#The file Lab5A.txt contains a list of IP address.  Write a program that will load the IP addresses into an array and then print only the class B addresses along with the subnet mask 255.255.0.0.
#----------------------------------------------------------------------------------------------


import csv


with open("C:/2a/Lab5A.txt") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        zero = row[0]

        classB = zero.split(".")

        subnet = "255.255.0.0"

        #print(x)

        if (classB[0] >= "128" and classB[0] <= "191"):
            print("{:15} {:20}" .format(zero, subnet))
            

    