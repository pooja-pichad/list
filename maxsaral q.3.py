# Code likho jo iss list mein se maximum dhund kar ke print kare.
 
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 

# # Iss list ke liye aapke program ka output 70 hona chaiye.
i=0
a=numbers[i]
while i<len(numbers):
    if numbers[i]>=a:
       a=numbers[i]
    # print(a)
    i=i+1
print( a)


# unorder_list = [6,8,4,3,9,56,0,34,7,15]
# def unorder_list(a):
#     print(sorted(a))
# unorder_list = ([6,8,4,3,9,56,0,34,7,15])