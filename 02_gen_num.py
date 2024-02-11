import re
from typing import Callable
from functools import reduce

text = """Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, 
доповнений додатковими надходженнями 27.45 і 324.00 доларів."""


def generator_numbers(txt: str):
    nums = map(float, filter(lambda x: re.match(r"[0-9]",x), txt.split()))
    for num in nums:
        yield num



def sum_profit(text, gen: Callable):
    return reduce(lambda x,y:x+y, gen(text))

total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")

