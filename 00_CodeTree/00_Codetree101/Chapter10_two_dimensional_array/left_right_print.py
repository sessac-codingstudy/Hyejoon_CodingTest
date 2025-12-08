"""
파일명: left_right_print.py
작성일: 2025-12-08
문제 링크: https://www.codetree.ai/ko/trails/complete/curated-cards/nl-pre-2d-array-pattern-printing-1/description
백준 난이도: 모름
체감 난이도: ⭐⭐⭐

설명: 2차원 배열 패턴 출력
"""
n = int(input())

for i in range(n):
    cnt = 1
    row = []
    
    for j in range(n):
        row.append(cnt)
        cnt += 1
    
    if i % 2 != 0:
        row.reverse()
        for j in range(n):
            print(row[j], end='')
    else:
        for j in range(n):
            print(row[j], end='')
    
    print()