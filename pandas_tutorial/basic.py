import pandas as pd
import numpy as np
import random
import string
from icecream import ic

np.random.seed(50)

pd.DataFrame({}, index =[])

df = pd.DataFrame({"a": [1,2], "b": [3,4], "c": [5,6]} , index =[1,2]) # ""컬럼, []데이터, index 인덱스
ic(df)
#리스트로 생성하는 방법
df2 = pd.DataFrame([[1,2,3],[4,5,6]], index=[1,2], columns=['a','b','c'])
ic(df2)

def id(): return''.join(random.choice(string.ascii_letters)for i in range(5))
def score(): return np.random.randint(0,101)

#데이터 프레임을 생성자로 생성한 방식
grade = pd.DataFrame([[score() for i in range(1,5)] for i in range(1,11)], index=[id() for i in range(1,11)], columns=['국어','영어','수학','과학'])
ic(grade)

#딕셔너리+loc를 활용해서 생성하는 방법
grade2 = pd.DataFrame({"국어":score(), "영어":score(), "수학":score(), "과학":score() }, index=[id()])
for i in range(1,11):
    grade2.loc[id()] = {"국어":score(), "영어":score(), "수학":score(), "과학":score() }
ic(grade2)
