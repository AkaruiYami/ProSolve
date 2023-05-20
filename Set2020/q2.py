def count_rectangle(m, n):
    return (m * (m+1) * n * (n+1)) // 4

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    print(count_rectangle(x-1, y-1))
