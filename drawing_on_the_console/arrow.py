n = int(input())

print('.' * (n // 2) + '#' * n + '.' * (n // 2))

for i in range(n - 2):
    print('.' * (n // 2) + '#' + '.' * (n - 2) + '#' + '.' * (n // 2))

mid = n - 2
left_right = (n * 2 - mid) // 2

print("#" * left_right + '.' * mid + "#" * left_right)

total = n + left_right + left_right - 2
mid = total - 4
left_right = 1
for i in range(n - 2):
    print('.' * left_right + "#" + '.' * mid + '#' + '.' * left_right)
    mid -= 2
    left_right += 1

print('.' * (total // 2) + '#' + '.' * (total // 2))