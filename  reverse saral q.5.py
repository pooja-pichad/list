# Code likho jo neeche di gayi lists ke items ko reverse order yaani ki ulta print kare.
 
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 

# Aapke code ka outut yeh hona chaiye:
# Hints

# Jab index i hai, tab length - i -1 index par kya hoga.
#  places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"


b=[]
i=1
while i<=len(places):
    b.append(places[-i])
    i=i+1
print(b)
