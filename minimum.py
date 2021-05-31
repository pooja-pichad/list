a=[9,3,4,7,8,1,11,12]
i=0
small=a[i]
while i<len(a):
    if a[i]<small:
        small=a[i]
    i=i+1
print(small)