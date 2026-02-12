# sol2) 수열 규칙 이용

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)

first = nums[0]
second = nums[1]
total = 0

# 가장 큰 수가 더해지는 횟수
count = M//(K+1) * K
count += M % (K+1)

# 가장 큰 수 더하기
total += count * first
# 두 번째로 큰 수 더하기
total += (M-count) * second

print(total)