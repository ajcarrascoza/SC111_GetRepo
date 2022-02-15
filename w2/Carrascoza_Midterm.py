#Andy Carrascoza
#Midterm
#202220_SE126.02 Intermediate Prog Using Python
#Write a program in Python that reads the data stored in the “midterm.csv” file and stores its data into separates lists. Once the lists have all been populated, process the lists to display all records that have 40 or more points. Next, process the lists again to determine the average number of hits. Last, display all records, one record per line.

#Variables
#Over - The amount of players that have hits over 40
#average - The average amount of hits in total
#total_hits - The total amount of hits all together
#amount_hits - The number of hits there to be divided by
#--------------------------------------

import csv

over = 0
average = 0
total_hits = 0
amount_hits = 0

with open("C:/2a/Midterm.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:

        playerName = (row[0])
        playerRace = (row[1])
        playerCharacter = (row[2])
        hits = int(row[3])
        if (row[3] >= "40"):
            overName = playerName
            overRace = playerRace
            overCharacter = playerCharacter
            overHits = hits
            over += 1
            print("{:9} {:12} {:9} {:4}".format(overName, overRace, overCharacter, overHits))


        amount_hits += 1
        total_hits += hits 
        average = total_hits
        average /= amount_hits

       

    print("The number of players with 40 or more hits: {0}".format(over))
    
    print("\nThe average number of hits: {:.2f}".format(average))

     
         




