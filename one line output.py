
# n=[[1,2,3],[4,5,6],[7,8,9]]
# n1=[num2 for num1 in n for num2 in num1]
# print (n1) #Output:[1, 2, 3, 4, 5, 6, 7, 8, 9]

n1=[[1,2,3],[4,5,6],[7,8,9]]
n2=[]
for num1 in n1:
 for num2 in num1:
  n2.append(num2)
print (n2) #Output:[1, 2, 3, 4, 5, 6, 7, 8, 9]

