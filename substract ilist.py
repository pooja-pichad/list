l1 = [10, 20, 30, 40, 50, 60]
l2 = [60, 50, 40, 30, 20, 10]
a= []
# i=0 
for i in range(len(l1)):
    if l1[i] > l2[i]:
        a.append(l1[i] - l2[i])
    else:
        a.append(l1[i])
          
print("Original list are :")
print(l1)
print(l2)
  
print("\nOutput list is")
print(a) 



# while i<len(l1):
#     if l1[i]>l2[i]:
#         a.append(l1[i]-l2[i])
#     else:
#         a.append(l1[-i])
#     i=i+1
# print("original list is:")
# print(l1)
# print(l2)

# print("output of given list:")
# print(a)