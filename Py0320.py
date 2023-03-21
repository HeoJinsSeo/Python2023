from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
DATA=PATH='/content/drive/MyDrive/data/'

# 데이터 불러오기
google = pd.read_csv(DATA_PATH + 'google.csv')
google.head()

google.info()

# 날짜 데이터 타입 배우기
# time_stamp 공식 문서
import pandas as pd
from datetime import datetime
time_stamp = pd.Timestamp(datetime(2023,3,20))

print(type(time_stamp))

pd.Timestamp('2023-03-20')

# 몇가지 옵션 확인
# 연도 추출
time_stamp.year

time_stamp.month
time_stamp.day
time_stamp.dayofweek

# 요일 구하세요
time_stamp.day_name()

#pd.Period
tmp_period = pd.Period('2023-03')
tmp_period #월을 호출

# 캘린더 데이 ---> 월의 마지막 날짜 호출
# 비즈니스 데이
tmp_period.asfreq('D')

tmp_period.to_timestamp().to_period('M')

# 임의의 시계열 데이터 생성
index = pd.date_range(start='2023-01-01',periods=12,freq='M')
index

# 데이터 프레임으로 변환
result = pd.DataFrame({'date': index})
result.info()

import numpy as np
data = np.random.random(size=(12,2))
data

# 데이터 프레임으로 변환
# 시계열 분석에서 아래 형태로 만들어야 함
result = pd.DateFrame(data=data, index=index)
result.head()

result.info()

# 반복문 문제
day_7=pd.date_range('2023-3-20',periods=7)
day_7
# 반복문을 활용해서 dayofweek, day_name()을 활용해서
# 리스트로 변환할 필요 없음
# 예시 출력
# 0 Monday
# 1 Tuesday
for day in day_7:
    print(day.year,day.dayofweek,day.day_name().day.month)
    
google = pd.read_csv(DATA_TATH + 'google.csv')
google.info()

# 날짜 데이터 객체로 변환하면, year,month 등등 편안하게 사용가능
# object를 날짜 데이터 객체로 변환
google['Date']= # 코드 형변환
    
google['Date']= pd.to_datetime(google['Date'])
google.info()

google.head()

google2 = google.copy()
google2 = google.set_index('Date')
google2.head()   

google2.info()

google2['Close'].plot(title='Stock Price')

# indexsing
google2.loc['2023'].head()

google2.loc['2023-3':'2023-8'].head()

# 특정한 날짜의 종가 구하기
google2.loc['2023-3-20','Close']

# 캘린더 데이, 비즈니스 데이
google2.asfreq('D').head() # 캘린더 데이

google2.asfreq('B').head()

yahoo = pd.read_csv(DATA_PATH + 'yahoo.csv')
yahoo['date']=pd.to_datetime(yahoo['date'])
yahoo=yahoo.set_index('date')
yahoo.head()

result1 = yahoo.loc['2013',['price']].reset_index(drop=True)
result1 = result1.rename(columns={'price':'2013'})

result2 = yahoo.loc['2014',['price']].reset_index(drop=True)
result2 = result2.rename(columns={'price':'2014'})

result3 = yahoo.loc['2015',['price']].reset_index(drop=True)
result3 = result3.rename(columns={'price':'2015'})

final_result = pd.concat([result1,result2,result3],axis=1)
final_result

# 반복문을 이용해서 코드짜기
# 빈 데이터프레임 객체
datas = pd.DataFrame()

years = ['2013','2014','2015']
for year in years:
    result1 = yahoo.loc[year,['price']].reset_index(drop=True)
    result1 = result.rename(columns={'price':year})
    # 저장한 후 업데이트
    datas = pd.concat([datas,result1],axis=1)
datas

# 범위가 넓어질 때 반복문 코드
datas = pd.DataFrame()

years = list(range(2013,2016))
for year in years:
    year = str(year)
    result1 = yahoo.loc[year,['price']].reset_index(drop=True)
    result1 = result1.rename(columns={'price':year})
    # 저장한 후 업데이트
    datas = pd.concat([datas,result1],axis=1)
datas

# 데이터 시각화의 기본 조건
# - 목적에 맞는 그래프 선정
# - 선형그래프, 막대그래프, 산점도, 박스플롯, etc
# 환경에 맞는 도구 선택
# - 코드기반 (R.Python)
# 프로그램 기반(시각화 등)
# - PowerB1, Tableau, Excel
# 문맥에 맞는 색과 도형 사용 

# 라이브러리 --> Matplotlib + Seaborn
# Matplotlib --> 정형 데이터 시각화
# - 시각화 문법이 어렵다
# - 데이터 프레임에서 쉽게 시각화 구현이 어려움
# Seaborn --> 디자인이 예쁘지 않다. 
# - Matplotlib를 보완하는 기능으로 사용해야 한다.
# Seaborn +Matplotlib 장점 위주 혼용


########## 오후 수업 코드 ############
!pip install -U matplotlib
# matplotlib 라이브러리 불러오기↑

# 런타임 재시작
import matplotlib as mpl
print(mpl.__version__)

# 데이터 자료
dates = [
    '2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05',
    '2021-01-06', '2021-01-07', '2021-01-08', '2021-01-09', '2021-01-10'
]
min_temperature = [20.7, 17.9, 18.8, 14.6, 15.8, 15.8, 15.8, 17.4, 21.8, 20.0]
max_temperature = [34.7, 28.9, 31.8, 25.6, 28.8, 21.8, 22.8, 28.4, 30.8, 32.0]

# 여기부터 시작
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(16,6)) #객체 선언
# 내부 시각화 코드 디테일하게 작성
ax.plot(dates,min_temperature,label = 'Min. Temp') # 라인 그래프
ax.plot(dates,max_temperature,label = 'Max. Temp') # 라인 그래프
ax.legend() # 범례
plt.show()


import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()

########## 주가 데이터 불러오기 #########
!pip install yfinance --upgrade --no-cache-dir

import yfinance as yf
data = yf.download("TSLA",start="2021-10-01",end="2023-03-17")
data.head()

aapl_close = data['Close']
aapl_close.head()

apple = yf.download("AAPL",start="2021-10-01",end="2023-03-17")
apple2 = apple['Close']
apple2.head()

## 라인 그래프 작성 시작
fig, ax = plt.subplots(figsize=(16,6))
ax.plot(aapl_close, label='TESLA')
ax.plot(apple2, label='APPLE')
ax.legend()
ax.set_xlabel('Date') # 가로 라벨 Date
ax.set_ylabel('Close Price') # 세로 라벨 Close Price
ax.set_title('Stock Market APPLE') # 제목 라벨
plt.show()

## 막대그래프
import matplotlib.pyplot as plt
import numpy as np
import calendar

month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
sold_list = [300, 400, 550, 900, 600, 960, 900, 910, 800, 700, 550, 450]

# 막대 그래프 # 틀 만들기 (상자)↓
fig, ax = plt.subplots(figsize=(16,6))
## barplots --> 막대그래프
barplots = ax.bar(month_list,sold_list)
for rect in barplots:
    print(type(rect),rect)
    height=rect.get_height()
    print(height) # 막대그래프 위로 숫자 생성↓
    ax.text(rect.get_x()+rect.get_width() / 2, 1.01*height, height, ha='center', va='bottom')
# 막대그래프 아래쪽이 월을 입력
plt.xticks(month_list, calendar.month_name[1:13],rotation=90)
plt.show()

## 히스토그램
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# 데이터 불러오기
titanic = sns.load_dataset('titanic')
# 데이터 가공하기
age = titanic['age']
# 데이터 시각화 --> x,y 좌표축 표의 틀
fig, ax = plt.subplots(figsize=(10,6))
# 메인 시각화 작성 --> 히스토그램 생성
ax.hist(age, bins=30)
## 세부 그래프를 추가 --> 평균값을 표시
ax.axvline(x=age.mean(),linewidth=2,color='r')
ax.text(37,70,'Mean of Age', horizontalalignment='center',verticalalignment='center')
plt.show()  # 텍스트 쓰기↑


