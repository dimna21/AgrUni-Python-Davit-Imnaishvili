import math

def triangle():
  a = int(input("Side a: "))
  b = int(input("Side b: "))
  c = int(input("Side c: "))
  if a+b <= c or a+c <= b or b+c <= a:
    print('Invalid sides for a triangle')
  else:
    perimeter = a+b+c
    x = perimeter/2
    area = math.sqrt(x*(x-a)*(x-b)*(x-c))
    print(f"Area: {area}, Perimeter: {perimeter}")

