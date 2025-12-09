N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)

first = nums[0]
second = nums[1]
total = 0
cnt = 0

# sol1) 무지성 greedy
while True:
    for i in range(K):
        total += first
        cnt += 1
        if cnt == M:
            break
    total += second
    cnt += 1
    if cnt == M:
        break

print(total)

# sol2) 수열 규칙 이용