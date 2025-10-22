def fibonacci():
  n = int(input("Enter n: "))

  a = 0
  b = 1
  ls = []
  for i in range(n):
      ls.append(a)
      temp = a
      a = b
      b = temp + b
  print(ls)

fibonacci()