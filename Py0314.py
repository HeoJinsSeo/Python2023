# 파이썬 기초 문법
# 여러줄 주석처리 시, 함수, 클래스 작성할 때
# 요긴하게 쓰임 
'''
여러줄 주석 처리
'''
"""
여러줄 주석 처리
"""
print("Hello World")

# 변수의 종류(Scala자료형)
# 크게 4가지 존재 : int, float, bool, None
# 스칼라의 의미 : 더 이상 나누어지지 않는 것
temp_int = 1
print(temp_int)
print(type(temp_int))

# 문자열
temp_int = '1'
print(temp_int)
print(type(temp_int))

# float형 예제
# 실수형
num_float = 0.2
print(num_float)
print(type(num_float))

# Bool형
# 참, 거짓
temp_bool = True
temp_bool = False
print(type(temp_bool))

# None 자료형
# Null을 나타내는 자료형
# 데이터 분석에서 가장 처리하기 까다로운 자료형
temp_none = None
print(type(temp_none))

# 사칙연산
# 정수형 사칙연산
a = 6
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)

# 실수형 사칙연산
a = 6.0
b = 2.0
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)

# 논리형 연산자
# AND조건, OR조건이 있음
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# 비교연산자
# 비교연산자는 부등호를 의미함
# 왼쪽이 기준 값
print(4>3)
print(3>4)
print(3>=4)
print(3<=4)

# input()
# print(): 출력
# input(): 입력
var = input("값을 입력해주세요!!")
print(var)
print(type(int(var)))

num1 = input("값을 입력해주세요!!")
num2 = input("값을 입력해주세요!!")
result = int(num1) + int(num2)
print(result)

# String
# 매우 중요함
str1 = "Hello"
str2 = "World"
print(str1 + str2)

str1 = "Hello"
str2 = "World"
result = str1 + str2
print(result)

str1 = "55"
str2 = "1000"
print(int(str1) + int(str2))

# 곱셈연산자 사용
greeting = "Hello World"
print(greeting*3)

# Indexing
# 0번째부터 시작
greeting = "Hello World!"
print(greeting[-4])

# 슬라이싱 : 자름
greeting = "Hello World"
print(greeting[0:5])
print(greeting[:])
print(greeting[6:])
print(greeting[3:8])
print(greeting[5:-1])
print(greeting[0:9:2])

greeting = "Hello World!!!!"
greeting[20]

# 문자열의 함수들
# 공식문서
tmp_string = 'Java'
# 변수명 저장!
# 변수명 저장함과 동시에, 클래스로 바뀜
print(tmp_string.lower())
print(tmp_string.upper())

tmp_string = "BMW-BENZ-TESLA-KIA"
# 공식문서에서 split 찾아보기
# 문자열의 단어 목록을 구분 기호 문자열로 
# 구분하여 반환합니다.
print(tmp_sting.split('-'))

# 리스트 
# 자바의 배열
a = []
a_func = list() # list()함수로도 빈 리스트 생성
b = [1]
c = ['Apple']
d = [1,2,['apple']]
print(a)
print(a_func)
print(b)
print(c)
print(d)

# 중첩리스트 (Nested List)
# 리스트내의 또 다른 리스트
a = [['apple','banana','cherry'],1]
print(a)
# cherry 글자에서 알파벳 e만 가져오세요
print(a[0][2][2])

a = [['apple','banana','cherry'],1]
temp = a[0]
temp2 = temp[2]
temp2[2]