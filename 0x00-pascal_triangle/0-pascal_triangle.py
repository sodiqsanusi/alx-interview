"""
The goal is to take in a number, and output a list of lists replicating
the Pascal's Triangle.

[1]
[1,1]
[1,2,1]
[1,]

"""


def pascal_triangle(n):
  lilac = []
  if n <= 0:
    return (lilac)
  elif n >= 1:
    lilac.append([1])
  for i in range(n - 1):
    violet = []
    temp = [0] + lilac[-1] + [0]
    for j in range(len(lilac[-1]) + 1):
      violet.append(temp[j] + temp[j + 1])
    lilac.append(violet)

  return (lilac)