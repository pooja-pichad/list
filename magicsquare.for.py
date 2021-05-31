magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 
a=[]
for i in range(3):                      #for row
    for j in range (3):
        # print(magic_square[i][j])
        # a.append()
        print()
sumd1=0
sumd2=0
for i in range (3):                         #for column
    for  j in range(3):
        if i==j:
            sumd1=sumd1+magic_square[i][j] 
        if i+j==3-1:
            sumd2=sumd2+magic_square[i][j] 
print(sumd1)
print(sumd2)
if sumd1!=sumd2:
    f=1
else:
    for i in range(3):                      # for diagonal
        sumr=0
        sumc=0
        for j in range(3):
            sumr=sumr+magic_square[i][j]
            sumc=sumc+magic_square[i][j]
        if sumr!=sumd1:
            f=1
        elif sumc!=sumd1:
            f=1
        else:
            f=0
print(sumr)
# print(sumc)
if f==0:
    print("matrix is magic square....")
else:
    print("matrix is not magic square")
