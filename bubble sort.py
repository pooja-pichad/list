a=[1,3,6,7,13,10,12]
i=0
# print(a)
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j=j+1
    i=i+1
print(a)
b=[]
i=1
while i<=len(a):
    b.append(a[-i])
    i+=1
print(b)


# a=[10,2,4,1,6]
# i=0
# print(a)
# while i<len(a):
#     j=0
#     while j<i:
#         if a[i]<a[j]:
#             temp=[i]
#             a[i]=temp
#         j=j+1
#     i=i+1
# print(a)