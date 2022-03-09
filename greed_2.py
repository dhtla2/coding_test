import time

start_time = time.time()

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    result = max(min(data), result)
end_time = time.time()

print(result)
print(end_time - start_time)