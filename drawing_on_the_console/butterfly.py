n = int(input())

for i in range(1, n - 1):
    if i % 2 == 1:
        print('*' * (n - 2) + chr(92) + " " + "/" + "*" * (n - 2))
    else:
        print('-' * (n - 2) + chr(92) + " " + "/" + "-" * (n - 2))

print(" " * (n - 1) + "@" + " " * (n - 1))

for i in range(1, n - 1):
    if i % 2 == 1:
        print('*' * (n - 2) + "/" + " " + chr(92) + "*" * (n - 2))
    else:
        print('-' * (n - 2) + "/" + " " + chr(92) + "-" * (n - 2))
