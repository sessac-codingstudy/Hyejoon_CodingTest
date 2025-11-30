"""
파일명: 25305_cutline.py
작성일: 2025-12-01
문제 링크: https://www.acmicpc.net/problem/25305
백준 난이도: Bronze 2
체감 난이도: ⭐⭐⭐

설명: 내림차순 정렬 문제
"""
n, k = map(int, input().split())
score = []
score = list(map(int, input().split()))
# print(score)
score.sort(reverse=True)
print(score[k-1])