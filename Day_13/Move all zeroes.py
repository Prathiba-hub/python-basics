n = int(input())
strings = []

for _ in range(n):
    strings.append(input().strip())

for s in strings:
    sorted_string = ''.join(sorted(s, reverse=True))
    print(sorted_string)
