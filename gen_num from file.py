import re


def generator_numbers(path: str):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            for txt in line.split():
                yield txt


sallary = 0
for l in generator_numbers("text.txt"):
    patern = r"[0-9]"
    if re.match(patern,l):
        num = float(l) 
        sallary = sallary + num
print (sallary)    