def has_duplicates(lis):
  lis1=sorted(lis)
  for item in range (len(lis1)-1):
    if lis1[item]==lis1[item+1]:
      return True
  return False
l=[2,3,4,5,6,6,4]
print(has_duplicates(l))