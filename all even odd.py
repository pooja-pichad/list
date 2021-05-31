# all are here, count , avg,sum/
# Ek code likho jo kisi bhi list ke liye yeh output karta hai, ki uss list mei odd numbers,
#  even numbers aur sab numbers ka: - count

# sum
# average

# print aaye.
# Sample Input
 
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
 
even_count=0
odd_count = 0
sum1=0
sum2=0
i= 0    
while(i < len(elements)):
    if elements[i] % 2 == 0:
        print("even number=",elements[i])
        sum1=sum1+elements[i]
        even_count += 1
    else:
        print("odd number=",elements[i])
        sum2=sum2+elements[i]
        odd_count += 1       
    i=i+1
avg=sum1/4
avg2=sum2/7
print("Even numbers count : ",  even_count,  "sum=",sum1,  "average=",avg)
print("Odd numbers count : ",   odd_count,   "sum=",sum2,  "average=",avg2)
