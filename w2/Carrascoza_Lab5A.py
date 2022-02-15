import csv


with open("C:/2a/Lab5A.txt") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        zero = row[0]

        B = zero.split(".")

        subnet = "255.255.0.0"

        #print(x)

        if (B[0] >= "128" and B[0] <= "191"):
            print("{:15} {:20}" .format(zero, subnet))
            

    