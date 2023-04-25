import numpy as np
from datetime import datetime
import pandas as pd

# 함수에 기준이 되는 컬럼을 매개변수 생성
# 매개변수 2개 구매 시기와 판매 시기

def bnh (x, col, start, end):
    
    x.index = pd.to_datetime(x.index)
    
    start = datetime.strptime(start, '%Y%m%d')
    end = datetime.strptime(end, '%Y%m%d')
   
    x = x.loc[start : end]
    
    # 결측치, 무한대 제외
    x = x.loc[~x.isin([np.nan, np.inf, -np.inf]).any(axis = 'columns')]
    
    # 수정 종가만 있는 데이터프레임으로 변경
    x = x[[col]]    
    
    # 일별 수익률 변수 생성
    x['daily_rtn'] = x[col].pct_change()
    
    # 누적 수익률 변수 생성
    x['st_rtn'] = (1+ x['daily_rtn']).cumprod()
   
   # 데이터프레임 리턴 
    return x
