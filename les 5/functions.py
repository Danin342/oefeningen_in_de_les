
def rng(list):
  return max(list) - min(list)


print(rng([4,0,1,-2]))

def swapFS(list):
  if len(list) > 1:
    list[0], list[1] = list[1], list[0]
  return list
print(swapFS(['one', 'two', 'three']))