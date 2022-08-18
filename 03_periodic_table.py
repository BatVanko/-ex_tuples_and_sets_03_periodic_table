n = int(input())
result = set()
for _ in range (n):
    current_set = set(input().split())
    result = result.union(current_set)

print(*result, sep='\n')