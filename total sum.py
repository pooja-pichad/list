# How to find all pairs in an array of integers whose sum is equal to the given number?
 
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19] 
# Output: [[11,19], [12,18],[13,17]]
# Edit on Github




i=0
y=[]
while i<len(n):
    a=0
    while a<len(n):
        if n[i]+n[a]==number:
            y.append([n[i],n[a]])
        if a==3:
            break
        a=a+1
    i=i+1
print(y)