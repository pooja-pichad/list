a=[1,2,3,[5,6,8],[6,7],[7,8]]
print(len(a))
i=0
new1=[]
sum1=0
while i<len(a):
    if i < 3:
        sum1=sum1+a[i]
        new1.append(a[i])
    else:
        j = 0
        while j < len(a[i]):
            sum1 = sum1 +a[i][j]
            new1.append(a[i][j])
            j = j + 1
    i = i + 1
print(sum1)
print(new1)


