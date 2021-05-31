# # Code likho jo iss list mein se second maximum element (doosra sabse bada element)
#  dhund kar kar print kare.
 
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 

# Iss list ke liye apke program ka output 56 hona chaiye.
i=0
k=numbers[0]
a=[]
while i<len(numbers):
    num=numbers[i]
    if num>k:
        k=num
    i=i+1
numbers.remove(k)
j=0
m=numbers[0]
s=[]
while j<len(numbers):
    n=numbers[j]
    if n>m:
        m=n
    j=j+1
a.append(m)
print(a)


