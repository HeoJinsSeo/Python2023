# Numpy 라이브러리 불러오기

import numpy as np
print(np.__version__)

import numpy
print(numpy.__version__)

# 리스트를 배열로 변환
# 리스트는 쉼표가 있음
# 배열은 쉼표가 없음
temp = [1,2,3,4,5,6,7,8,9,10]
temp_array = np.array(temp)
print(temp)        # 리스트
print(temp_array)  # 배열

print(type(temp))       # 리스트
print(type(temp_array)) # 배열
print(temp_array.shape)
print(temp_array.ndim)

temp_array[1]

temp_array[-1]

# 사칙연산
score1 = [10,15,40,50,80]
score2 = [30,40,70,50,100]
score1 + score2

# 리스트를 사칙연산이 가능한 numpy로 변형해서 계산
score1_arr = np.array(score1)
score2_arr = np.array(score2)
result = score1_arr + score2_arr

np.min(result)
np.max(result)

np.sum(result)

# 배열(행렬)의 생성
# 0차원부터 3차원까지로 구성 
temp_arr = np.array(30)
print(temp_arr)
print(type(temp_arr))
print()
print(temp_arr.shape)

temp_arr = np.array([1,2,3])
print(temp_arr.shape)
print(temp_arr.ndim)  # 1차원 배열

# 2차원
# 정형 데이터 (엑셀 데이터)
temp_arr = np.array([[1,2,3],[4,5,6]])
print(temp_arr.shape)
print(temp_arr.ndim) # 1차원 배열

# 3차원 데이터
# 이미지 데이터
temp_arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(temp_arr.shape)
print(temp_arr.ndim)

temp_arr = np.array([1,2,3,4], ndmin = 3)
print(temp_arr.shape)
print(temp_arr.ndim)

# 배열 생성의 다양한 방법들
# 모두 0으로 채운다
temp_arr = np.zeros((5,10))
temp_arr.dtype  # 배열 요소가 실수형 타입 1., 1., ...

temp_arr = np.ones((5,10))
temp_arr

# 임의의 상수값으로 채운다
temp_arr = np.full((2,3),10)
temp_arr

# 최소 및 최대 숫자의 범위를 정해두고, 구간별로
# 값을 생성하는 코드를 작성함
temp_arr = np.linspace(5,1000,5)
temp_arr   # 5와 1000사이에 5개의 숫자 생성

# 범위를 구하는 배열
# np.arange()
temp_arr = np.arange(1,100,4)
# 1부터 100사이에 숫자중 1부터 시작해서 4씩
# 커지는 숫자를 나열
temp_arr

# 임의의 난수 생성 (3가지 방법이 있음)
from numpy.random import rand
x = rand()
print(x)

from numpy import random
x = random.rand()
print(x)

import numpy as np
x = np.random.rand()
print(x)

# 배열 연산
# 덧셈: np.add()
# 뺄셈: np.subtract()
# 곱셈: np.multiply()
# 나눗셈: np.divide()
import numpy as np
array_01 = np.array([1,2,3])
array_02 = np.array([10,20,30])
## 덧셈
result = np.add(array_01,array_02)
result
## 뺄셈
result = np.subtract(array_01, array_02)
result
## 곱셈
result = np.multiply(array_01,array_02)
result
## 나눗셈
result = np.divide(array_01, array_02)
result

array_01 = np.array([1,2,3])
array_02 = np.array([1,2,3])
result = np.power(array_01, array_02)
print(result)

# 소숫점 정렬
# 소숫점 절삭
# 프로그램 코드는 실행속도를 체크
# 어떤 함수가 속도가 빠른지를 체크해서 시간 절약

%%time
temp_arr = np.trunc([-1.23,1.23])
print(temp_arr)

%%Time
temp_arr = np.fix([-1.23,1.23])
print(temp_arr)

# 소수점 자리에서 반올림
temp_arr = np.around([-1.123131,1.123131],3)
temp_arr

temp_arr = np.round([-1.123131,1.123131],3)
temp_arr

# 소수점을 모두
temp_arr = np.floor([-1.23456,1.23456])
print(temp_arr)

import time
start_time = time.time() #현재시간 저장
# 실행시간을 측정하고자 하는 코드

temp_arr = np.floor([-1.23456,1.23456])
print(temp_arr)
end_time = time.time() #현재 시간을 저장
elapsed_time = end_time - start_time #코드실행 시간 계산
print("코드 실행 시간 : ", elapsed_time, "초")

# 조건문
# where : 조건식 1개일 때 활용
# select : 다중조건일 때 활용
temp_arr = np.arange(10)
temp_arr

# np.where (조건식, 참일때, 거짓일때)
np.where(temp_arr < 5, temp_arr, 10*temp_arr)

# np.select(유용한 함수, 자주 이용됨)
temp_arr = np.arange(10)
cond_list = [temp_arr>5, temp_arr<2]
choice_list = [temp_arr*3, temp_arr+10]
np.select(cond_list, choice_list, default=temp_arr)
