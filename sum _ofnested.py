a=[1,2,[4,5],7,9,[10],4,6,[4,6,7,8,9],2]
i=0
sum=0
while i<len(a):
    n=a[i]
    if type(n)==list:   
        for j in range(len(n)):
            sum=sum+n[j]
    else:
        sum=sum+n
    i=i+1
print(sum)