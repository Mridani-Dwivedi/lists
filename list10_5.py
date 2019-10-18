def is_sorted(lis):
  if lis==sorted(lis):
    return True
  return False
lis=['d','e','f','a','b']
print(is_sorted(lis))