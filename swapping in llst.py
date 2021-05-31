

newList = [12, 35, 9, 56, 24]
i=0
size = len(newList)
while i<size:
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    i=i+1 
print (newList)
