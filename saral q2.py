# Code likho jo di gayi list mein jo number 20 se bade
#  hai aur 40 se chote hai unhe count kare. aur count print kare

 
numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 



i=0
count=0
while i<len(numbers):
    a=numbers[i]
    if a>20 and a<40:
        count=count+1
        print(a)
    i=i+1
print("count","=",count)