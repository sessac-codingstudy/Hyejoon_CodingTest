"""
파일명: up_down_print.py
작성일: 2025-12-08
문제 링크: https://www.codetree.ai/ko/trails/complete/curated-cards/nl-pre-2d-array-pattern-printing-2/description
백준 난이도: 모름
체감 난이도: ⭐⭐⭐

설명: 2차원 배열 패턴 출력
"""


n = int(input())
mat = [[0 for _ in range(n)] for _ in range(n)]
# print(mat)

for i in range(n):
    cnt = 1
    if i % 2 != 0:
        for j in range(n-1, -1, -1):
            mat[j][i] = cnt
            cnt += 1
    else:
        for j in range(n):
            mat[j][i] = cnt
            cnt += 1

for i in range(n):
    for j in range(n):
        print(mat[i][j], end="")
    print()