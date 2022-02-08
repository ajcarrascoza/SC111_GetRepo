import array as arr

import csv

over = 0
line = 0
maxLine = 10




with open("C:/2a/Lab2b-1.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        over = over + 1
        cpu = row[2]
        ram = row[3]
        hdd1 = row[4]
        num_hdd = row[5]
        if(row[0] == "D"):
            computer_type = "Desktop"
        else:
            computer_type = "Laptop"

        if(row[1] == "DL"):
            manufacturer = "Dell"

        elif(row[1] =="HP"):
            manufacturer = "HP"
        
        elif(row[1] == "GW"):
            manufacturer = "Gateway"

        if(row[5] == "1"):
            os = row[6]
            year = row[7]
            hdd2 = ""

        else:
            hdd2 = row[6]
            os = row[7]
            year = row[8]

            

        print("{:9} {:9} {:5} {:4} {:10} {:10} {:10} {:3} {:2}".format(computer_type, manufacturer, cpu, ram, hdd1, num_hdd, hdd2, os, year))



   

