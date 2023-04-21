n = int(input())
left_right = n // 2
mid = (n * 2) - (left_right * 2) - 4

print('/' + "^" * left_right + "\\" + "_" * mid + "/" + "^" * left_right + "\\")

for i in range(n - 3):
    print('|' + " " * ((n * 2) - 2) + '|')

print('|' + " " * (left_right + 1) + "_" * mid + " " * (left_right + 1) + "|")
print('\\' + "_" * left_right + "/" + " " * mid + "\\" + "_" * left_right + "/")
