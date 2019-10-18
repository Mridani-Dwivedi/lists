import time
def fun1():
  fin=open('words.txt')
  lis=[]
  for word in fin:
    word=word.strip()
    word=word.split()
    #print(word)
    lis.append(word)
  #print(lis)
def fun2():
  fin=open('words.txt')
  lis=[]
  for word in fin:
    word=word.strip()
    word=word.split()
    #print(word)
    lis=lis+[word]
  #print(lis)
strt=time.time()
fun1()
print(strt,"-",time.time())
strt=time.time()
fun2()
print(strt,"-"time.time())
