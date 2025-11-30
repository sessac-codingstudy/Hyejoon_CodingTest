"""
파일명: selection_sort.py
작성일: 2025-12-01
문제 링크: 이것이 코딩테스트다 with 파이썬 책 예시코드
백준 난이도: 
체감 난이도: ⭐

설명: 선택 정렬 예시코드
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i   # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap
