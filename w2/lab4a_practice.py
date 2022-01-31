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
        ram = int(row[3])
        typeList.append(row[0])
        brandList.append(row[1])
        cpuList.append(row[2])
        ramList.append(row[3])
        diskList.append(row[4])
        hddList.append(row[5])
        disk2List.append(row[6])
        osList.append(row[7])
        if ram > 8:
          over += 1


print("Type =",typeList, "\n")
print("Brand =",brandList, "\n")
print("CPU =",cpuList, "\n")
print("RAM =",ramList, "\n")
print("1st Disk =",diskList, "\n")
print("No HDD =",hddList, "\n")
print("2nd Disk =",disk2List, "\n")
print("OS =",osList, "\n")
print("Year =",yrList, "\n")

print("{0} computers have more than 8GB of RAM".format(over))