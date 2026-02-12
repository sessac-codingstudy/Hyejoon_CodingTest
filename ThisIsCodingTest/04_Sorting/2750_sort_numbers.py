"""
파일명: 2750_sort_numbers.py
작성일: 2025-12-01
문제 링크: https://www.acmicpc.net/problem/2750
백준 난이도: Bronze 2
체감 난이도: ⭐

설명: 파이썬의 내장 라이브러리 함수 사용하면 쉬움
"""
n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))

num_list.sort()

for i in range(n):
    print(num_list[i])