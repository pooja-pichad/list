
# Make a list by taking 10 input from user. Now delete all repeated elements of the list.
# E.g.-
a= [1,2,3,2,1,3,12,12,32]
# OUTPUT : [1,2,3,12,]
i=0
while i<len(a):
    j=i+1
    j=1
    while j<len(a):
        if a[i]==a[j]:
            del(a[i])
        j=j+1
    i=i+1
print(a)
