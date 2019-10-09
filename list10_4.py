#Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None
lis=[1,2,6,2,5,1,2,4,3]
def chop(lis):
    del lis[0]
    del lis[-1]
    print(lis)
print(chop(lis))  