# Write a program to check if elements of a list are same or not it read 
# from front or back. E.g.-

a=[1,2,7,8,6,4,7,8,9,10]
i=0
m=len(a)
num=int(input("enter a number:-"))
while i<m:
    if a[i]==num:
        print(f"{a[i]} are same as {num}")
        break
    else:
        print("both are not same")
        break
    i=i+1
