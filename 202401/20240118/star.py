# 1
for line in range(1,6) :
    print('*' * line + ' ' * (5 - line))

print('----------')

# 2
for line in range(1,6) :
    print(' ' * (5 - line) + '*' * line)

print('----------')

# 3
for line in range(1,6) :
    print('*' * (6 - line) + ' ' * (line - 1))

print('----------')

# 4
for line in range(1,6) :
    print(' ' * (line - 1) + '*' * (6 - line))

print('----------')

# 5
for line in range(1,6) :
    print(' ' * (5 - line) + '*' * (2 * line - 1) + ' ' * (5 - line) )

print('----------')

# 6
for line in range(1,6) :
    print(' ' * (line - 1) + '*' * (2 * (6 - line) - 1) + ' ' * ((line - 1) ))

print('----------')

# 7
for line in range(1,10) :
    print(' ' * abs(5 - line) + '*' * (2 * (5 - abs(5 - line)) - 1) + ' ' * abs(line - 5))

print('----------')

# 8
for line in range(1,10) :
    print('*' * (5 - abs(5 - line)) + ' ' * (2 * abs(5 - line)) + '*' * (5 - abs(5 - line)))

print('----------')

# 9
for line in range(1,10) :
    print(' ' * (5 - abs(5 - line)) + '*' * (2 * abs(5 - line)+1) + ' ' * (5 - abs(5 - line)))