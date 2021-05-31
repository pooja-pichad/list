# Occurences - occur shabd se bana hai, 
# jiska matlab hota hai, ki kitni baar aata hai. Sample List
 
l = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 

# Sample List ka Output:
 
# [["a", 6], ["n", 3], ["t", 2], ["x", 2], ["u", 1], ["g", 1]]
 

# k=[]
# i=0
# while i<len(char_list):
#     j=0
#     count=0
#     a=[]
#     while j<len(char_list):
#         if char_list[i]==char_list[j]:
#             count=count+1
#         j=j+1
#     a.append(char_list[i])
#     a.append(count)
#     if a not in k:
#         k.append(a)
#     i=i+1
# print(k)



i=0
a=[]
while i<len(l):
    b=l[i]
    if b not in a:
        a.append(b)
    i=i+1
print(a)