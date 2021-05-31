

# Find largest and smallest elements of a list.

a=[1,3,4,7,8,9,11,12]
i=0
large=a[i]
while i<len(a):
    if a[i]>large:
        large=a[i]
    i=i+1
print(large)