
# Take 10 integer inputs from user and store them in a list and print them on screen.

# k=[]
# i=10
# while i>0:
#     num=int(input("enter a numbers"))
#     k.append(num)
#     i=i-1
# print(k)




# Take 10 integer inputs from user and store them in a list. 
# Again ask user to give a number. Now, tell us
# er whether that number is present in list or not.
# k=[]
# i=10
# while i>0:
#     num=int(input("enter a numbers"))
#     k.append(num)
#     i=i-1
# print(k)
# n=int(input(" check any number present in our list"))
# i=9
# count=0
# while i>=0:
#     if n==k[i]:
#         print("yes it is precent in list")
#         count=count+1
#     i=i-1
# if count==0:
    # print("no")
# if n in a:
#     print("yes yes")
# else:
#     print("no no")




# take 20 integer inputs from user and print the following:
# number of positive numbers
# number of negative numbers
# number of odd numbers
# number of even numbers
# number of 0s.

i=20
k=[]
while i<0:
    num=int(input("enter a number"))
    k.append(num)
    i=i-1
print(k)
# n=int(input("enter a number for check"))
even=0
odd=0
zero=0
positvie=0
negatvie=0
i=19
while i>=0:
    if k[i]==1:
        zero=zero+1
    elif k[i]>0:
        positvie=positvie+1
        if k[i]%2==0:
            even=even+1
        else:
            odd=odd+1
    else:
        negavtive=negavtive+1
    i=i-1
print("EVEN=",even,"odd=",odd,"zero=",zero,"positvie=",positvie,"negavtive=",negavtive)

     