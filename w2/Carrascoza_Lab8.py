
def seatMap():
    seatTemplate = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
    heading = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4']
    map = []
    
    map.append



a = [['a', 'b', 'c'],['d', 'e', 'f'],['l','m','n']]

#search = input("enter: ")

for row in range (0, 3):
 for col in range (0, 3):
     print(a[0][col], end= "")
print()


def ticketPurchase():
    #row = input("Enter your row choice: ")
    #col = input("Enter your seat choice: ")
    a = [['1', '2', '3', '4', '5'],['6', '7', '8', '9', '10'],['11','12','13','14', '15']]

    for row in range (0, 3):
     for col in range (0, 5):
         print(a[row][col], end= "")
    print()


ticketPurchase()