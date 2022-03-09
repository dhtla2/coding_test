import time

N, M, K = map(int, input().split())
input_num = list(map(int, input().split()))
start_time = time.time()

result = 0
input_num.sort(reverse=True)

count = (int(M / (K+1)) * K) + (M % (K+1))
result += count * input_num[0]
result += (M - count) * input_num[1]
print(result)

end_time = time.time()
print(end_time - start_time)