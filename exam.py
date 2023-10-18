grid = {'A':'123456789', 'B':'123456789', 'C':'123456789',
        'D':'123456789','E':'123456789','F':'123456789',
        'G':'123456789', 'H':'123456789','I':'123456789'}

for key, value in grid.items():
    available_digits = set("123456789")
    for digit in value:
        if digit in available_digits:
            grid[key] = digit
            available_digits.remove(digit)
            break

print(grid)
