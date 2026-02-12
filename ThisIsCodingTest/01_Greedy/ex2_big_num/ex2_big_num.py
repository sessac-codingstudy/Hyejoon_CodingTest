# sol1) 무지성 greedy

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)

first = nums[0]
second = nums[1]
total = 0
cnt = 0

while True:
    for i in range(K):
        total += first
        cnt += 1
        if cnt == M:
            break
    if cnt >= M:
        break
    total += second
    cnt += 1
    

print(total)