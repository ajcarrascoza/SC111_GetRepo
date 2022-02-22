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
     first1 = row[0]
     last1 = row[1]
     phone1 = row[2]
     addy2 = row[3]
     department1 = row[4]
     place1 = row[5]
     first.append(row[0])
     last.append(row[1])
     phone.append(row[2])
     addy.append(row[3])
     department.append(row[4])
     place.append(row[5])

     #addy3 = addy2.replace(".com", ".net")
           
     #print(com)

 
    
    #print("Name =", )
    #print("Pos= ", pos)

     length = len(department)
     found = "False"
     search = "MIS"

     for pos in range(0, length):
            #print(last[pos])
         if(search == department[pos]):
             found = "True"
             position = pos
             amount += 1
             
     if found == "True":
         addy3 = addy2.replace(".com", ".net")
         print(first1, last1, phone1, addy3, department1, place1)

    print("\nNumber of employees who work for the company: {0}".format(amount))

 


     
        

