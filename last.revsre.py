a=[1,2,3,4,5,6,7,8,9,10]
num=int(input(" enter the number :-"))
i=1
k=[]
while i<=num:
    k.append(a[-i])
    i=i+1
print(k)