# challenge 1

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  print(sum)
# challenge 2
def largest(nums):
  largestNum = 0
  for num in nums:
    if num > largestNum:
      largestNum = num
  print(largestNum)

# challenge 3
def occurrances(str1, str2):
  print(str1.count(str2))

# challenge 4

def product(*args):
  total = 1
  for num in args:
    total *= num
  print(total)
