n = int(input())
left_right = n + 1
mid = n * 2 + 1

print('.' * left_right + '_' * mid + '.' * left_right)

for i in range(n):
    print('.' * (left_right - 1) + "//" + '_' * (mid - 2) + '\\\\' + '.' * (left_right - 1))
    left_right -= 1
    mid += 2

mid -= 5

print('//' + '_' * ((mid // 2) - 1) + "STOP!" + '_' * ((mid // 2) - 1) + "\\\\")

mid += 5

for i in range(n):
    print('.' * (left_right - 1) + "\\\\" + '_' * (mid - 2) + '//' + '.' * (left_right - 1))
    left_right += 1
    mid -= 2

