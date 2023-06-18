def add(*arg):
  print(arg)
  sum = 0
  for n in arg:
    sum = sum + n
  return sum


print(add(1, 2, 3, 4))


def calculate(n, **kyarg):
  print(kyarg)
  for key, value in kyarg.items():
    print(key)
    print(value)

  n += kyarg["add"]
  n *= kyarg["multiply"]
  print(n)


calculate(2, add=2, multiply=4)
