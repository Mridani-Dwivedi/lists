#Write a function called nested_sum that takes a list of lists of integers and adds up the elements from all of the nested lists.

def nested_sum(lis):  
  tot=0
  for i in lis:
    if type(i)==list:

      tot=tot+nested_sum(i)
    else:
      tot=tot+i
  
  return tot
lis=[1,2,3,4,[5,6,7],8,[9,10]]
print(nested_sum(lis))