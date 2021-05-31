a=["70","90","67c","77"]
i=0
sum=0
while i<len(a):
    n=a[i]
    if type(int)==list:
        for j in range(len(n)):
            sum=sum+n[j]
    else:
        sum=sum+n
    i=i+1
print(sum)