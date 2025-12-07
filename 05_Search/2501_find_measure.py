"""
파일명: 2501_find_measure.py
작성일: 2025-12-08
문제 링크: https://www.acmicpc.net/problem/2501
백준 난이도: Bronze 3
체감 난이도: ⭐⭐

설명: 약수 구하기 문제 (Greedy) -> 조건 줘서 끝까지 안 찾아도 되게 하기
"""



# # sol1) 완전탐색(greedy) => 런타임 에러가 나옴
# n, k = map(int, input().split())
# list = []

# for i in range(n):
#     if n % (i+1) == 0:
#         list.append(i+1)
# # print(list)
# print(list[k-1])

# sol2) k번째까지만 찾기
n, k = map(int, input().split())

for i in range(1, n+1):
    if n % (i) == 0:
        k -= 1
        if k == 0:
            print(i)
            break
else:
    print(0)