def filljug(jug, cap):
    curr=0
    while(curr!=cap):
        jug+=1

def emptyjug(jug):
    jug=0

def pour(jug1, jug2, cap1, currentcap1):
    currentcap1 = jug2 = cap1


"""jug1 = int(input("Enter capacity of jug 1 : "))
jug2 = int(input("Enter capacity of jug 2 : "))
target = int(input("Enter target volume: "))
 """

jug1, jug2, target= 3, 4, 2

temp =0
tempvol1=0
tempvol2=0

print("( {},{} )".format(jug1, jug2))

while True:
    if temp == target :
        break
    else:
        filljug(tempvol2, jug2)
        print("( {},{} )".format(tempvol1, tempvol2))
