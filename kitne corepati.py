# Kitne Crorepati?
 
kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 

# Aapko ek aisa program likhna hai jo, bataye, ki uppar wali list mei kitne log: Jaise, 
# uppar wali list ke liye aapka output hoga:
 
# 4 Crorepati hai
# 3 Lakhpati hai
# 4 Dilwale hai 

i=0
a=0
b=0
d=0
while i<len(kitna_paisa_hai):
    p=kitna_paisa_hai[i]
    if p>=10000000:
        a=a+1
    elif p>=100000:
        b=b+1
    elif p<=100000:
        d=d+1
    i=i+1
print(a,"corepati hai")
print(b,"lakhpati")
print(d,"dilwale hai")