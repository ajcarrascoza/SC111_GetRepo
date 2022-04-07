import csv

over = 0

typeList = []
brandList = []
cpuList = []
ramList = []
diskList = []
hddList = []
disk2List = []
osList = []
yrList = []




with open("C:/2a/Lab2b-1.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        over = row[3]
        typeList.append(row[0])
        brandList.append(row[1])
        cpuList.append(row[2])
        ramList.append(row[3])
        diskList.append(row[4])
        hddList.append(row[5])
        if(row[5] == "1"):
            osList.append(row[6])
            yrList.append(row[7])
        else:
          disk2List.append(row[6])
          osList.append(row[7])
          yrList.append(row[8])
        

print("Type =",typeList, "\n")
print("Brand =",brandList, "\n")
print("CPU =",cpuList, "\n")
print("RAM =",ramList, "\n")
print("1st Disk =",diskList, "\n")
print("No HDD =",hddList, "\n")
print("2nd Disk =",disk2List, "\n")
print("OS =",osList, "\n")
print("Year =",yrList, "\n")

name = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]

if(name == "16GB"):
  over += 1




print("{0} computers have more than 8GB of RAM".format(over))