#to find upper case letters in list
t=['a','b','c','D','F','G','h']
def cap(t):
  res=[]
  for i in t:
    if i.isupper():
      res.append(i)
  print(res)
cap(t)