# Ek code likho jo kisi bhi list ke liye yeh output karta hai,
#  ki uss list mei kitne odd numbers hai aur kitne even numbers hai.
 
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
# Edit on Github

even_count=0
odd_count = 0
i= 0    
while(i < len(elements)):
    if elements[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    i=i+1
print("Even numbers : ", even_count)
print("Odd numbers : ", odd_count)
