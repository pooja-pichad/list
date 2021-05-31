# FLOATS ki LIST

# Yeh pichle saat dinon mein temperatures ki list hai.
 
# temperature_list = [21.1, 24.3, 19, 25, 17, 18, 23]
# print (temperature_list) 

# Lekin hum jab bhi ek list variable pe type function ka use karenge, 
# toh humesha uska type list dikhayega. Lekin list ke andar kuch bhi type ho sakte hain.



# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)
# i=0
# while i<len(mylist):


lst = ["a", "b", "a", "c", "c", "a", "c"]
temp=len(lst)
result=[]
for i in temp:
    result[i]=lst.count(i)
print (result)


