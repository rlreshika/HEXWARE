def lin_search(ar,match):
  for i in range(len(ar)):
    if ar[i] == match:
      return i
  return -1
 
ar = list(map(int,input().split()))
match = int(input())
 
print(lin_search(ar,match))
