def count_down(start):
    while start > 0:
        yield start
        start -= 1

for number in count_down(5):
    print(number)
