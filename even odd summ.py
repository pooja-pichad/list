# Ek code likho jo kissi bhi list ke liye uss list ke do sum ka output karta hai, 
# ki uss list mei odd numbers ka sum aur even numbers ka sum kitna hai.
 
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
# Edit on Github
# i= 0  
# sum1=0
# sum2=0  
# while(i < len(elements)):
#     if elements[i] % 2 == 0:
#         sum1=sum1+elements[i]
#     else:
#         sum2=sum2+elements[i]
#     i=i+1
# print("Even numbers : ", sum1)
# print("Odd numbers : ", sum2)




i= 0  
sum1=0
sum2=0  
while(i < len(elements)):
    if elements[i] % 2 == 0:
        print("even",elements[i])
        sum1=sum1+elements[i]
    else:
        print("odd",elements[i])
        sum2=sum2+elements[i]
    i=i+1
print("Even numbers : ", sum1)
print("Odd numbers : ", sum2)




# 