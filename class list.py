# list=[]
# i=0
# while i<10:
#     list.append(i)
#     i=i+1
# print(list)


# a=[1,2,3,4,5,6,7]
# b=[]
# b.append(a)
# print(b)


n=[[1,2,3,4],[5,6,7,8]]
i=0
while i<len(n):
    j=0
    while j<len(n[i]):
        print(n[i][j])
        j=j+1
    i=i+1


    # elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 

# even_count=0 
# odd_count = 0
# for i in elements:
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
          
# print("Even numbers : ", even_count)
# print("Odd numbers : ", odd_count)