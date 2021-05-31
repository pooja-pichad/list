# ss program mei humein agar koi number binary form mei diya gaya hai, toh hum uski decimal form nikalna seekhenge.
# content

# Jaise yeh diagram dekho.
 
binary_number = [1, 0, 0, 1, 1, 0, 1, 1] 

# Iss number ko decimal form mei karne ke liye, hum
 
# last element ko 2^0 yaani 1 se
# second last element ko 2^1 yaani 2 se
# third last element ko 2^2 yaani 4 se
# fourth last element ko 2^3 yaani 8 se
# ...
# ...
# 
# multiply kar kar
# add karna hai 

# Aise karne se uppar wali list ka answer 155 aayega

i=0
sum=0
while i<len(binary_number):
        rem=binary_number[len(binary_number)-i-1]
        sum=sum+rem*(2**i)
        # print(sum)
        i=i+1
print(sum)





# i=0
# sum=0
# l=len(binary_number)
# while i<len(binary_number):
#     num=binary_number[l-i-1]
#     sum=sum+num*(2**i)
#     i=i+1
# print(sum)