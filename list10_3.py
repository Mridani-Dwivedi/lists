#Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. 

def middle(lis):
 lis1=[]
 lis1=lis1+lis[1:-1]
 
 return lis1


lis=[1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
print(middle(lis))