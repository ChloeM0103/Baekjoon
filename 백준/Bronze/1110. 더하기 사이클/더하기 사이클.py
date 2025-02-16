A= int(input()) 
Original = A
cycle = 0
while True:
  i = A // 10 
  j = A % 10
  new_j = (i+j) % 10
  A= j * 10 + new_j
  cycle = cycle + 1
  if Original == A:
    break
print(cycle)