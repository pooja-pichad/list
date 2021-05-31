# Iss list ko dekhein:
 
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 

# Yeh kisi student ke peechle teen saal ke marks hai. 
# Aap ko jitne bhi saal hai, har saal ke average marks print karne hai. 
# Jaise, uppar wali list ka output yeh hona chahiye:



i=0
avg=0
count=0
while i<len(marks):
    sum=0
    a=0
    s=0
    while a<len(marks[i]):
        s=s+marks[i][a]
        a=a+1
    sum=sum+s
    avg=sum//len(marks[i])
    i=i+1
    count=count+1
    print(count,"year avg",avg)


# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ] 
# i=0
# avg=0
# count=0
# while i<len(marks):
#     sum=0
#     a=0
#     s=0
#     while a<len(marks[i]):
#         s=s+marks[i][a]
#         a=a+1
#     sum=sum+s
#     avg=sum//len(marks[i])
#     i=i+1
#     count=count+1
#     print(count,"year avg",avg)


# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78],
#     [87, 67, 49, 68, 88]
# ] 
# i=0
# avg=0
# count=0
# while i<len(marks):
#     sum=0
#     a=0
#     s=0
#     while a<len(marks[i]):
#         s=s+marks[i][a]
#         a=a+1
#     sum=sum+s
#     avg=sum//len(marks[i])
#     i=i+1
#     count=count+1
#     print(count,"year avg",avg)






