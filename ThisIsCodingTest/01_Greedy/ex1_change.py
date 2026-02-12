"""
파일명: ex1_change.py
작성일: 2025-12-09
문제 링크: .\Hyejoon_CodingTest\01_Greedy\00_Greedy.md
백준 난이도: 
체감 난이도: ⭐

설명: Greedy(탐욕법) 유형 예제 문제
이것이 코딩테스트다 예제3-1 거스름돈(p.87)
"""

n = int(input())
cnt = 0
coin_list = [500, 100, 50, 10]

for coin in coin_list:
    cnt += n // coin
    n = n % coin

print(cnt)