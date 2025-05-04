lst =  [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

n = int(input())
if n == 0 or n < 0 or n > 3999:
    print("Roman numerals typically support values 1 - 3999.")
    exit()

roman = ""

while(n):
    for val in lst:
        if val[0] <= n:
            roman += val[1]
            n -= val[0]
            break

print(roman)