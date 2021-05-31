# a=[1,2,3,4,5,6,7,8,9]


# sum1=0
# sum2=0

# i=0
# n=a[i]
# while i<len(a):
#     if (i<n//2):
#         sum1+=a[i]
#     else:
#         sum2+=a[i]
#     i=i+1
# print(sum1,sum2)
# print(sum2)







a=[1,2,3,5,6,2,3,3,2,1]
print(len(a))
i=0
new1=[]
new2=[]
sum1=0
product=1
while i<len(a):
    if i < 5:
        sum1=sum1+a[i]
        new1.append(a[i])
    else:
        product=product*a[i]
        new2.append(a[i])
    i = i + 1
# print(sum1)
print("addition: ",new1,"sum:",sum1)
print("multiply:",new2, "multiply:",product)
# print(p)