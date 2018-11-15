


# smallest number

import intertools

number='907'
# print(len(number))
permutations = itertools.permutations(number, 3)
new = []

for i in permutations:
  # print(i)
  a=''.join(i)
  b=int(a)
  # print(b)
  new.append(b)
# print(new)
another = []
for j in range(0, 907):
  if j in new:
    # print(j)
    another.append(j)
print(another[-1])






def fib(n):
    cur = 1
    old = 1
    i = 1

    while (i < n):
        cur, old, i = cur+old, cur, i+1
        return cur
