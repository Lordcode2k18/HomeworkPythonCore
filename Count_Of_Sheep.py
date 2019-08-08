def count_sheeps(arrayOfSheeps):
  i=0
  count_sheeps=0
  while i<len(arrayOfSheeps):
      if arrayOfSheeps[i]==True:
          count_sheeps+=1
      i+=1    
  return count_sheeps