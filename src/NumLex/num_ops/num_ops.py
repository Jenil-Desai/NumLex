def max_num(data: list[float]) -> float:
    maxValue = data[0]
    for i in data:
        if i > maxValue:
            maxValue = i
    return maxValue

def min_num(data: list[float]) -> float:
    minValue = data[0]
    for i in data:
        if i < minValue:
            minValue = i
    return minValue

def total_num(data: list[float],option: str = "simple") -> float:
    res = 0
    if option.lower() == "odd":
        for i in data:
           if i % 2 == 1:
            res = res + i
    elif option.lower() == "even":
        for i in data:
           if i % 2 == 0:
            res = res + i
    else:
       for i in data:
            res = res + i
    return res

def is_negative(num: int) -> bool:
   if num > 0:
    return True
   else:
    return False
   
def is_positive(num: int) -> bool:
   if num < 0:
    return True
   else:
    return False

def is_odd(num: int) -> bool:
   if num % 2 == 1:
    return True
   else:
    return False
   
def is_even(num: int) -> bool:
   if num % 2 == 0:
    return True
   else:
    return False
   
def is_leap(year: int) -> bool:
   if year % 4 == 0:
    return True
   else:
    return False
   
def num_len(num: int) -> int:
  cnt = 0

  while num != 0:
    num = num // 10
    cnt += 1

  return cnt

def digit_sum(num: int) -> int:
  res = 0

  while num != 0:
    digit = num // 10
    res = res + digit
    num = num // 10

  return res

def num_rev(num: int) -> int:
   return int(str(num)[::-1])

def is_palindrome(num: int) -> int:
   if num == num_rev(num):
    return True
   else:
    return False