# Palindrome or not?

# Palindrome wo strings ya numbers hote hai jo ulta seedhe same hote hai. Jaise, NITIN. Nitin ko aap left se padho ya right se, nitin hi hai. 
# Aise hi MOM bhi ek palindrome hai. 
# Code likho jo check kare ki kya list palindrome hai ya nahi. 
# Aur print karo “Haan! palindrome hai” agar hai. 
# Aur “nahi! Palindrome nahi hai” agar nahi hai. 
# Abhi ke liye iss list ko use kar ke code likh sakte ho:
 
name=[ 'n', 'i', 't', 'i', 'n' ] 

# Apni list ko change kar ke alag alag values ke saath test out
#  karo aur fir finally theek code ko upload karo. 
#  Inn values ke liye aap test kar sakte hai nayan => true naina => 
#  false anamana => true ainaania => true ainabnia => false

i=len(name)-1
n=name
temp=[]
while i>=0:
    t=(name[i])
    temp.append(t)
    i=i-1
print(temp)
if temp==n:
    print("its palindrome ")
else:
    print("its not palindrome ")




