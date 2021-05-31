# Average Kitna Hai

# Ek code likho jo kissi bhi list ke liye uss list ke do average ko output karta hai, 
# ki uss list mei odd numbers ka average aur even numbers ka average kitna hai.
 
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 

i= 0  
sum1=0
sum2=0  
while(i < len(elements)):
    if elements[i] % 2 == 0:
        sum1=sum1+elements[i]
    else:
        sum2=sum2+elements[i]
    i=i+1
avg=sum1/4
avg2=sum2/7
print("Even numbers : ", sum1,"/", "avrage=",avg)
print("Odd numbers : ", sum2,"/","average=",avg2)

