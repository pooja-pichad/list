
# Write a program to print sum, average of all numbers, smallest and largest element of a list.
# a=[8,4,3,2,6,7,9,10,12,34,75]
# i=0
# sum=0
# while i<len(a):
#     b=a[i]
#     if a[i]>b:
#         b=a[i]
#     sum=sum+b
#     i=i+1
# print("large",b)
# print("sum",sum)
# avg=sum/11
# print( "averge",avg)

# samllest code


a=[9,3,4,7,8,1,11,12]
i=0
small=a[i]
while i<len(a):
    if a[i]<small:
        small=a[i]
    i=i+1
print(small)