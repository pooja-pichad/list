#  Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which numbers 
#  are not present in the second array.
 
list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7] 

# i=0
# b=[]
# while i<1:
#     a=list1[3]
#     b.append(a)
#     j=0
#     while j<1:
#         b.append(list1[4])
#         j=j+1
#     i=i+1
# print(b)


i=0
b=[]
while i<len(list1):
    a=list1[i]
    if a not in list2:
        b.append(a)
    i=i+1
print(b)


