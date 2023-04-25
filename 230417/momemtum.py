import pandas as pd
import numpy as np
from datetime import datetime




def func_1 (df, col = 'Close', start = '20100101', end = '20230101'):
    
    
    
    # 인덱스가 Date가 아니면? Date컬럼을 인덱스로 변경
    if 'Date' in df.columns:
          df = df.set_index('Date')  
          
    # start, end 시계열로 변경
    start = datetime.strptime(start, '%Y%m%d').isoformat()
    end = datetime.strptime(end, '%Y%m%d').isoformat()
    
    # 결측치와 이상치 제거
    df = df.loc[~df.isin([np.nan, np.inf, -np.inf]).any(axis = 'columns')]
     
    # 수정종가를 제외한 나머지 컬럼 삭제
    df = df[[col]]
     
    # 인덱스를 시계열로 변경
    df.index = pd.to_datetime(df.index, format = '%Y-%m-%d')
    df = df.loc[start:end]
    
    # STD-YM 컬럼 생성
    df['STD-YM'] = list(map(lambda x : datetime.strftime(x, '%Y-%m'), df.index))     
     
    return df
 
  
def func_2(df):
    
    col = df.columns[0]
    
    # df2 = pd.DataFrame()
    # _list = df['STD-YM'].unique()
    #     last_df = df.loc[df['STD-YM'] == i].tail(1)
    #     df2 = pd.concat([df2,last_df])
    
    df2 = df.loc[df['STD-YM'] != df.shift(-1)['STD-YM']]
    df2['BF_1M'] = df2.shift(1)[col].fillna(0)
    df2['BF_12M'] = df2.shift(12)[col].fillna(0)    
    return df2    

def func_3(df1, df2):
    df1['trade'] = ''
    df1['return'] = 1
    col = df1.columns[0]
    rtn = 1.0
    Buy = 0
    Sell = 0 
    acc_rtn = 1.0
    
    for i in df2.index:
        signal = ''
        
        # 절대 모멘텀 계산
        momentum_index = df2.loc[i, 'BF_1M'] / df2.loc[i, 'BF_12M'] - 1 
        
        # 절대 모멘텀 지표에 따라서 True 와 False 로 구분
        flag = True if((momentum_index > 0) and (momentum_index != -np.inf) and (momentum_index != np.inf)) else False
        
        if flag : 
            signal = 'buy'
        
        print('날짜:', i, '모멘텀 인덱스:', momentum_index, "flag :", flag, "signal:", signal)
        df1.loc[i,'trade'] = signal
        

    for i in df1.index:
        if (df1.shift(1).loc[i,'trade'] =='') & (df1.loc[i,'trade'] =="buy"):
            Buy = df1.loc[i,col]
            print('진입일:', i, '구입가격:', Buy)
        elif (df1.shift(1).loc[i,'trade'] =='buy') & (df1.loc[i,'trade'] ==""):
            Sell = df1.loc[i,col]
            rtn = (Sell - Buy) / Buy + 1 
            df1.loc[i,'return'] = rtn
            print('판매일:', i, '판매가격:', Sell, '수익률:', rtn)
        
        acc_rtn *= df1.loc[i, 'return']
        df1.loc[i,'acc_rtn'] = acc_rtn

    return df1        