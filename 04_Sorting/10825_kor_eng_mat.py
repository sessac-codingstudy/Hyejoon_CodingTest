"""
파일명: 10825_kor_eng_mat.py
작성일: 2025-12-01
문제 링크: https://www.acmicpc.net/problem/10825
백준 난이도: silver 4
체감 난이도: ⭐⭐

설명: sorted() 함수의 key 매개변수를 활용한 정렬 문제
"""
n = int(input())
array = []

# 공백을 기준으로 튜플 형태로 입력받기
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
# print(array)

# sorted() 함수의 key 매개변수 조건설정
def setting(student):
    return student[1]

array = sorted(array, key=setting)
# lambda를 활용한 다른 방식
# array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')