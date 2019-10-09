#Write a function called cumsum that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i+1 elements from the original list.
def cumsum(lis):
  lis1=[]
  su=0
  for i in lis:
    su=su+i
    lis1=lis1+[su]
  print(lis1)
  return lis1
lis=[1,2,3,4,5,6,7,8,9,10]
print(cumsum(lis))