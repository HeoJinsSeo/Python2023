# 데이터 불러오기
DATA_PATH="/content/drive/MyDrive/Lemonade2016.csv"
DATA_PATH

import pandas as pd
lemonade = pd.read_csv(DATA_PATH)
lemonade

# 정보 확인
lemonade.info()

lemonade.head(3)
lemonade.tail(3)

# 기초 통계량 --> count, mean, std, min, max...
lemonade.describe()

# 문자형 데이터 갯수 파악 시, 유용하게 사용
lemonade['Location'].value_counts(normalize=True)

lemonade.head()

# 새로운 칼럼 추가
lemonade['Sold']= lemonade['Lemon'] + lemonade['Orange']
lemonade.head(3)

# Revenue 칼럼: 매출 계산
lemonade['Revenue']=lemonade['Price']*lemonade['Sold']
lemonade.head(3)

# axis = 1 컬럼을 삭제하겠다.
lemonade_col_drop = lemonade.drop('Sold',axis=1)
lemonade_col_drop.head(3)

# axis=0 조건에 맞는 행을 삭제하겠다.
lemonade_row_drop = lemonade.drop(0, axis = 0)
lemonade_row_drop.head()

# 행을 삭제한 후, 인덱스 번호를 초기화
# 0번째부터 순차적으로 시작하도록 변환
lemonade_row_drop = lemonade.drop(3,axis=0)
lemonade_row_drop.reset_index(drop=True)

# 데이터 인덱싱
lemonade[0:10:2]

lemonade[lemonade['Location'] == 'Beach']

lemonade['Location']=='Beach'

lemonade.head()

# iloc
lemonade.iloc[0:3,0:2]

lemonade.loc[0:2,['Date','Location']]

# 행과 열을 동시 처리 ---> loc만 처리
It = lemonade.loc[lemonade['Revenue']>100,['Date','Revenue']].reset_index(drop=True)
It

It = lemonade.loc[lemonade['Lemon']<100,['Date','Lemon','Sold']].reset_index(drop=True)
It

cols = ['Date','Orange','Revenue']
It = lemonade.loc[0:5,cols].reset_index(drop=True)
It

It = lemonade.iloc[0:5,0:3]
It

# 정렬
lemonade.sort_values(by=['Revenue'],ascending=False).head()

# ascending=False --> 내림차순 정렬, ascending=True --> 오름차순 정렬
lemonade[['Leaflets','Revenue']].sort_values(by=['Leaflets','Revenue'],ascending=[False,True]).head()

# ascending=False --> 내림차순 정렬
lemonade[['Leaflets','Revenue']].sort_values(by=['Leaflets','Revenue'],ascending=False).head()

lemonade.groupby(by='Location').count().T


# Aggregation 집계함수
import numpy as np
lemonade.groupby('Location')['Revenue'].agg([max, min, np.mean])

import numpy as np
lemonade.groupby('Location')[['Revenue','Temperature']].agg([max, min, np.mean, np.std, sum])

import seaborn as sns
import pandas as pd
import numpy as np
sns.get_dataset_names()


iris = sns.load_dataset('iris')
iris.head()

iris['sepal_length'].std()

iris.info()

iris.values

iris.shape

iris.values.shape

result = list(iris.colums)
result

# species칼럼이 setosa인 것만 조회
result = iris[iris['species']=='setosa']
result

result = list(iris.colums)
result

result = iris[iris['species']=='setosa']
result.head(3)

# sepal_width가 3보다 작은 데이터만 조회
result2 = result[result['sepal_width']<3].reset_index(drop=True)
result2

# And조건 &
# OR 조건 |
result3 = iris[(iris['species']=='setosa') & (iris['sepal_width']<3)].reset_index(drop=True)
result3