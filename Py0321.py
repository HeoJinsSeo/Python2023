## 시각화 리뷰
## matplotlib
import matplotlib as mpl
mpl.__version__

import matplotlib.pyplot as plt

## 데이터 가져오기 
## 데이터 가공 ---> 시각화로 그릴 데이터를 추출

# 시각화 코드 작성
fig, ax = plt.subplots()
ax.plot([1,2,3])
# 세부옵션
ax.set_xlabel('title')
ax.set_ylabel('sss')
ax.set_title('title')
plt.show()


!pip install yfinance --upgrade --no-cache-dir

import yfinance as yf

aapl = yf.download('AAPL',start = '2021-08-01',end = '2023-03-30')
aapl.head()

tsla = yf.download('TSLA',start= '2021-08-01',end = '2023-03-30')
tsla.head()


# 종가 시각화 그래프 작성
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(aapl['Close'], label = 'APPLE')
ax.plot(aapl['Close'], label = 'TESLA')
ax.legend()
plt.show()


def stockChart(ticker=None):
    data = yf.download(ticker,start='2021-08-01', end = '2023-03-30')
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(data['Close'], label = ticker)
    ax.legend()
    plt.show()
    
stockChart('APPLE')


stockChart('MSFT')

## 산점도 그래프
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
tips.head()

## 영수증 금액이 크면, 팁도 많이 줄까?
## 산점도 그래프, 두 개의 변수
## 연속형 수치형 데이터만 가능함

fig, ax=plt.subplots(figsize=(10,6))
ax.scatter(tips['total_bill'],tips['tip'])
ax.set_xlabel('Total Bill',size=16)
ax.set_ylabel('Tip',size=16)
plt.show()

## 그래프를 보고 설명가능 해야함
## 회귀분석

## 여성이랑, 남성이랑 구분해서 구분해서 시각화를 해볼래!! 
# 색상참조 : https://color.adobe.com/ko/create/color-wheel
label, data = tips.groupby('sex')
### 남자와 여자 색깔 구분
tips['sex_color'] = tips['sex'].map({"Female" : "#F000B3", "Male" : "#00FF00"})
print(tips.head())
fig, ax = plt.subplots(figsize=(10,6))
for label, data in tips.groupby('sex'):
    ax.scatter(data['total_bill'],data['tip'], label=label,
               color=data['sex_color'], alpha = 0.5)
    ax.set_xlabel('Total Bill')
    ax.set_ylabel('Tip')
    ax.set_title('Tip ~ Total Bill by Gender')
    
ax.legend()
fig.show()


## 게임사 기준 : 분석가 ---> 전략 기획 소속

## 박스 플롯
# - 그룹간의 평균을 비교 시각적으로 표현
# - 개별 분포 확인
# - 이상치(이상한 값, 튀는 값)확인
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
print(iris.head())

data = [iris[iris['species']=="setosa"]['petal_width'], 
        iris[iris['species']=="versicolor"]['petal_width'],
        iris[iris['species']=="virginica"]['petal_width']]

fig, ax=plt.subplots(figsize=(10,6))
ax.boxplot(data,labels=['setosa','versicolor','virginica'])   
plt.show()       


######## 한글폰트 ###########
# 아래 코드 설치후 런타임 재시작
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -ReferenceError


import matplotlib.pyplot as plt

plt.rc('font',family = 'NanumBarunGothic')
plt.plot([1,2,3])
plt.title('한글 잘 먹나요?',size = 20)
plt.show()


######## jupyter lab 에서 한글폰트 적용 예시
import matplotlib as mpl
print(mpl.matplotlib_fname())

print(mpl.get_cachedir())

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.family']= "KoPubWorldDotum"
mpl.rcParams['font.size']=10

plt.plot([1,2,3])
plt.legend(['가나다'])
plt.title("안녕하세요. 한글폰트입니다.")
plt.show()

##### Seaborn 라이브러리
# seaborn 은 matplotlib 기반으로 만들어진 라이브러리
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
fig, ax = plt.subplots()
sns.scatterplot(x = 'total_bill', y='tip', data=tips)

plt.show()
###########################

###########################
fig,ax = plt.subplots(nrows = 1, ncols = 2, figsize = (15,5))

sns.regplot(x = 'total_bill',
            y = 'tip',
            data = tips,
            ax = ax[1],
            fit_reg = True)
## ax = ax[]는 index를 의미
ax[1].set_xlabel('Bill',size=30)
ax[1].set_title('TITLE')

sns.regplot(x = 'total_bill',
            y = 'tip',
            data = tips,
            ax = ax[0],
            fit_reg = False)
## ax = ax[]는 index를 의미
ax[0].set_ylabel('Money',size=30)

plt.show()
################################

################################
fig, ax = plt.subplots(nrows = 4, ncols = 6, figsize=(16,10))
# 4 X 6 배열로 시각화 기본화면을 만들어보세요.
ax[1,4].set_title('dafdas')
plt.show()
################################

################################
# 히스토그램/ 커널 밀도 그래프
tips = sns.load_dataset('tips')
fig, ax = plt.subplots()
sns.histplot(x ='tip', data = tips, ax=ax )
ax.set_title('title')
ax.set_xlabel("tip",size=40)
plt.show()
#################################


sns.displot(x = 'tip', kde = True, data=tips)


#################################

## 박스플롯
# matplotlib로는 가공하기 힘들었음
sns.boxplot(x='day',y='total_bill',data=tips)


sns.countplot(x='day', data = tips)
plt.show()



## value_counts()
print(tips['day'].value_counts())


print(tips['day'].value_counts().index)


print(tips['day'].value_counts().values)


print(tips['day'].value_counts(ascending = True))


fig, ax = plt.subplots()
ax = sns.countplot(x = 'day', data=tips, order=tips['day'].value_counts().index)
print(type(ax))
plt.show()


fig, ax = plt.subplots()
ax = sns.countplot(x = 'day', data = tips, order =tips['day'].value_counts().index )
for p in ax.patches:
    print(p)
plt.show()



fig, ax = plt.subfdplots()
ax = sns.countplot(x = 'day',data = tips, order=tips['day'].value_counts().index) 
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width()/2., height+3, height, ha = 'center', size =9) 

ax.set_ylim(-5, 100)
plt.show()




# seaborn 참조 : https://seaborn.pydata.org/ 
 
 
## 성별을 나눠서 보도록 하자 ## hue = 'sex'추가
fig, ax = plt.subplots()
ax = sns.countplot(x = 'day', data=tips, hue = 'sex', order = tips['day'].value_counts().index)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width()/2., height+3, height, ha = 'center', size = 9)

ax.set_ylim(-5, 100)
plt.show()



## 상관관계 그래프
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

mpg = sns.load_dataset('mpg')
print(mpg.info())



###### 상관관계 계수 #######
# 상관관계 : 무조건 두 변수가 연속형 변수여야함 
# object 안됨

num_mpg = mpg.select_dtypes(include = np.number)
num_mpg.info()


num_mpg.corr()


## 참조 :  https://jehyunlee.github.io/2020/08/27/Python-DS-28-mpl_spines_grids/
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (16,5))
# 기본 상관관계 히트맵
sns.heatmap(num_mpg.corr(), ax=ax[0])
ax[0].set_title('Basic Correlation Heatmap', pad = 12)

# 상관관계 수치 그래프 [Correlation Heatmap with Number]
sns.heatmap(num_mpg.corr(), vmin = -1, vmax = 1, annot=True, ax = ax[1]) 
ax[0].set_title('Basic Correlation Heatmap', pad = 12) 

plt.show()
    
    
######### 코랩 단축키 ############
# ctrl + M + B : 코드추가
# ctrl + M + M : 텍스트추가
# ctrl + N : 새창
# ctrl + W : 창닫기


import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator, FuncFormatter)
import seaborn as sns 
import numpy as np

def major_formatter(x, pos):
    return "%.2f$"% x #21.10$
formatter = FuncFormatter(major_formatter)
tips = sns.load_dataset('tips')

## 데이터 가공
group_mean = tips.groupby(['day'])['total_bill'].agg('mean')
h_day = group_mean.sort_values(ascending=False).index[0]
h_mean = np.round(group_mean.sort_values(ascending=False)[0],2)
print(h_day, h_mean)

fig, ax = plt.subplots(nrows =1, ncols = 2, figsize = (16,5))
ax0 = sns.barplot(x = 'day', y='total_bill', data = tips, 
                  errorbar = None, color = 'lightgray',
                  alpha = 0.85, zorder = 2, ax = ax[0])
for p in ax0.patches:
    fontweight = 'normal'
    color = 'k'
    height = np.round(p.get_height(),2)
    if h_mean == height:
        fontweight = 'bold'
        color = 'darkred'
        p.set_facecolor(color)
        p.set_edgecolor("black")
    ax0.text(p.get_x() + p.get_width()/2., height + 1, height,
             ha = 'center', size = 12, fonweight = fontweight, color = color)       

# y축 변환
ax0.set_ylim(-3, 30)

# y축 타이틀
ax0.set_title('Ideal Bar Graph', size = 16)

# 옵션 1
ax0.spines["top"].set_visible(False)
ax0.spines["right"].set_visible(False)
ax0.spines["left"].set_visible(False)
ax0.spines["left"].set_position(('outward',20))  

# 옵션 2
ax0.yaxis.set_major_locator(MultipleLocator(10))
ax0.yaxis.set_major_formatter(formatter)
ax0.yaxis.set_minor_locator(MultipleLocator(5))

# 옵션 3
ax0.grid(axis = "y", which = "major", color="lightgray")
ax0.grid(axis = "y", which = "minor", Is=":")

ax0.set_xlabel('Weekday', fontsize = 14)
for xtick in ax0.get_xticklabels():
    print(xtick)
    if xtick.get_text() == h_day:
        xtick.set_color('darkred')
        xtick.set_fontweight('demibold')
ax0.set_xticklabels(['Thursday', 'Friday', 'Saturday', 'Sunday'], size=12) 
     
ax1 = sns.barplot(x = "day", y = 'total_bill', data = tips, 
                  errorbar = None, alpha = 0.85,
                  ax = ax[1])
for p in ax1.patches:
    height = np.round(p.get_height(), 2)
    ax1.text(p.get_x() + p.get_width()/2., height+1, height, ha = 'center', size = 12)
ax1.set_ylim(-3,30)
ax1.set_title("Just Bar Graph")

fig.show()

plt.show()

           






  