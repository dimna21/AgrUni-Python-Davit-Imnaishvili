def print_divisors():
  n = int(input("Enter number: "))
  for i in range(1, n + 1):
      if n % i == 0:
          print(i, end=" ")

print_divisors()
