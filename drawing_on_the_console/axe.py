n = int(input())
total = n * 5
left = n * 3
right = n * 2 - 2
mid = total - left - right - 2

for up in range(n):
    print('-' * left + '*' + '-' * mid + '*' + '-' * right)
    if up == n - 1:
        break
    right -= 1
    mid += 1

for mid_print in range(n // 2):
    print('*' * left + '*' + '-' * mid + '*' + '-' * right)

for down in range(n // 2):
    print('-' * left + '*' + '-' * mid + '*' + '-' * right)
    left -= 1
    right -= 1
    mid += 2
    if down == n // 2 - 2:
        print('-' * left + '*' + '*' * mid + '*' + '-' * right)
        break
