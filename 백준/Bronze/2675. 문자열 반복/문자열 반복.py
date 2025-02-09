T = int(input())
for i in range(T):
  i = input()
  first,second = i.split(" ")
  for j in second:
    print(j*int(first),end="")
  print("")