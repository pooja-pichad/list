marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 

# Yeh kisi student ke peechle teen saal ke marks hai. Aap ko teeno saalo, 
# ke sab subjects ke marks ka total calculate karna hai. Jaise uppar di hui 
# nested list ka sum - 1142 aayega. # Edge Cases: Check your program
#  for following nested lists as well (bina code change kiye chalna chahiye, 
#  nahi toh aapne sahi se code nahi likha):

i=0
sum=0
while i<len(marks):
    j=0
    s=0
    while j<len(marks[i]):
        s=s+marks[i][j]
        j=j+1
    sum=sum+s
    i=i+1
print(sum)
avg=sum/15
print("avg","=",avg)




# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ] 
# i=0
# sum=0
# while i<len(marks):
#     j=0
#     s=0
#     while j<len(marks[i]):
#         s=s+marks[i][j]
#         j=j+1
#     sum=sum+s
#     i=i+1
# print(sum)
# avg=sum/12
# print(avg)



# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78],
#     [87, 67, 49, 68, 88]
# ] 

# # Jaise uppar di hui nested list ka sum - 1324 aayega.
# i=0
# sum=0
# while i<len(marks):
#     j=0
#     s=0
#     while j<len(marks[i]):
#         s=s+marks[i][j]
#         j=j+1
#     sum=sum+s
#     i=i+1
# print(sum)
# avg=sum/17
# print(avg)



