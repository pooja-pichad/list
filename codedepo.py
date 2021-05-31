
# Take 10 integer inputs from user and store them in a list. Now, 
# copy all the elements in another list but in reverse order.


k=[]
i=10
while i>0:
    num=int(input("enter a number"))
    k.append(num)
    i=i-1
print( "list=",k)
a=[]
i=1
while i<=len(k):
    a.append(k[-i])
    i=i+1
print("reverse=",a)

