n = int(input())
l = list(map(int, input().split()))
print(max(n - l.count(max(l)) - l.count(min(l)), 0))
