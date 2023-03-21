# 리스트 연결 연산자
# 덧셈, 곱셈
a = ['alice','bob','cat']
b = ['apple','banana','cherry']

c = a + b
print(c)

a = ['a','b','c']
b = a*3
print(b)

c = a*0
print(c)

# 리스트 값 수정
a = [1,1,1]
a[1]= "b"
print(a)

# 리스트 값 추가하기
# append 메서드 사용
# 반복문 사용시, 매우 자주 활용됨
a = [100,200,300]
a.append(400)
a.append(500)
a.append(600)
print(a)

a = [100,200,300]
b = [400,500,600]
a.extend(b)
print(a)

# insert
# 특정한 위치에 값을 추가
a = [1,1,1,1,1,1,1] 
a.insert(2,100)
print(a)

# 리스트의 값을 삭제
# remove()함수
# remove에 숫자는 value값이다
a = [5,4,3,2,1]
a.remove(4)
a

# pop함수
# delete, 숫자는 index번호이다
a = [5,4,3,2,1]
a2 = a.pop(4)
print(a2)
print(a)

# 그 외 유용한 메서드
# clear함수
a = [1,4,5,2,3]
print(a)
a.clear()
print(a)

a = [1,4,5,2,3]
a.sort()  # 오름차순 정렬
print(a)

a = [1,4,5,2,3]
a.sort(reverse=True) # 내림차순 정렬
print(a)

# 튜플
tuple01 = (0)
tuple02 = (0,)
tuple03 = 0,1,2

print(tuple01)
print(tuple02)
print(tuple03)

print(type(tuple01))
print(type(tuple02))
print(type(tuple03))

# packing
my_tuple = 3,2,"A"
print(my_tuple)
# Unpacking
a,b,c = my_tuple
print(a)
print(b)
print(c)

# tuple(튜플)은 수정 삭제 안된다
a = [0,1,2,3,4,5,"a"]
del a[6]
a

# a = (0,1,2,3,4,5,"a")
# del a[6]
# a

# a = (1,1,1,'a')
# a[3] = 1
# a

a = [1,1,1,'a']
a[3] = 1
a

## 슬라이싱, 인덱싱

# 더하기 및 곱셈 연산자 사용
t1 = (0,1,2,3,4)
t2 = ('a','b','c')
print(t1 + t2)
print(t1*3)
print(t1*0)

# 딕셔너리
# key 와 value 로 이루어짐
# key : name, value : 홍길동
temp_dict = {
    "a" : [0,1,2,3],
    "b" : "휴먼",
    "c" : 100
}
temp_dict

temp_dict['a']

# temp_dict['d']: keyError --> 딕셔너리에 키 값이 
# 없다는 에러

print(type(temp_dict.keys()))
# 리스트로 변환
result = temp_dict.keys()
result.append("d")
result = list(temp_dict.keys())
print(result)
print(type(result))

result = temp_dict.values()
print(type(result))
print(result)

# 튜플과 리스트가 같이 나오는 경우
a = {'name' : '휴먼', 'age' : 50, 'job' : '학생'}
result = list(a.items())
print(result)
result[0][1]

a = -8
if a > 5:
    print("a가 5보다 크다")
elif a > 0:
    print("a가 0보다 크다")    
else: 
    print("음수")

# input 함수
# 90점 이상 A등급, 80점 이상 B등급, 나머지 C등급
var = int(input("입력하세요!!"))    
if var >= 90:
    print("A등급")
elif var >= 80:
    print("B등급")    
else:
    print("C등급")

var = input("입력하세요")
print(var)
print(type(var))

# 반복문
# Hello World 10개를 출력
a = "Hello World \n"
print(a*10)

# 과제 : Hello World 700개 출력
for i in range(700):
    print("Hello World")

letters = ['A','B','C']    
for idx, value in enumerate(letters):
    print(idx, value)

fruits = ['apple','kiwi','mango']    
# 리스트의 값 중에서 a가 들어간 글자만 따로 출력
# 리스트 컴프리핸션(List Comprehension)
newlists = [fruit for fruit in fruits if "a" in fruit]
print(newlists)

fruits = ['apple','kiwi','mango']
newlist = []
for fruit in fruits:
    print(fruit)
if "a" in fruit:
    newlist.append(fruit)
    print(newlist)
    
fruits = ['apple','kiwi','mango']
"a" in fruits[2]    
    