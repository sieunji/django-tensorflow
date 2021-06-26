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