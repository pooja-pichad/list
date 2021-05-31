# Magic Square woh square hota hai jismei - 
# har row ka, har column ka, and dono diagonals ka sum same hota hai. 
# Aapko yeh program likhna hai - jo ek nested list leta hai, 
# aur dekhta hai ki woh magic square hai ya nahi? E.g. Yeh magic square hai, kyuki
 
magic = [
    [8, 3, 4],
    [1, 5, 6],
    [6, 7, 2]
] 

i=0
k=0
while i<len(magic):
    j=0
    while j<len(magic):
        k=k+magic[i][j]
        j=j+1
        break
    i=i+1
print(k)
a=0
b=0
while a<len(magic):
    c=0
    while c<len(magic):
        b=b+magic[a][c]
        c=c+1
        break
    a=a+1
print(b)
x=0
y=0
while x<len(magic):
    z=0
    while z<len(magic):
        y=y+magic[x][z]
        z=z+1
        break
    x=x+1
print(y)
if k==b==y:
    print("magic square")
else:
    print("not magic sqaure")



