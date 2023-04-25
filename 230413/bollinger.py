import pandas as pd
import numpy as np
from datetime import datetime


# class 선언
class Invest:
    
    # 생성자 함수 생성
    def __init__(self, _df, _col):
        #self 변수는 클래스 각각의 독립적인 변수
        self.df = _df
        self.col = _col        
        

    def create_band (self, start, end):
    # 인덱스를 시계열로 변경
        self.df.index = pd.to_datetime(self.df.index)
        
        # start, end를 시계열로 변경
        start = datetime.strptime(start, '%Y%m%d').isoformat()
        end = datetime.strptime(end, '%Y%m%d').isoformat()
        
        
        #결측치와 이상치 제거
        self.df = self.df.loc[~self.df.isin([np.nan, np.inf, -np.inf]).any(axis = 'columns'), [self.col]]
        # self.df = self.df[[self.col]]
        
        #이동평균선 생성
        self.df['Center'] = self.df[self.col].rolling(20).mean()
        
        #상단밴드, 하단밴드 생성
        
        self.df['ub'] = self.df['Center'] + (2 * self.df[self.col].rolling(20).std())
        self.df['lb'] = self.df['Center'] - (2 * self.df[self.col].rolling(20).std())
        
        # 데이터를 시작시간부터 종료시간까지 필터링
        self.df = self.df.loc[start:end]
        
        return self.df

    #2번 함수 생성
    def add_trade (self):
       
        # trade 파생변수 생성
        self.df['trade'] = ''
        
        # 거래 내역 추가
        for i in self.df.index:
            if self.df.loc[i,self.col] > self.df.loc[i,'ub']:
                if self.df.shift(1).loc[i,'trade'] == 'buy':
                    self.df.loc[i,'trade'] = ""
                else:
                    self.df.loc[i,'trade'] = ""
            
            elif self.df.loc[i,self.col] < self.df.loc[i,'lb']:
                if self.df.shift(1).loc[i,'trade'] == 'buy':
                    self.df.loc[i,'trade'] = 'buy'
                else:
                    self.df.loc[i,'trade'] = 'buy'
            
            else:
                if self.df.shift(1).loc[i,'trade'] == 'buy':
                    self.df.loc[i,'trade'] = 'buy'
                else:
                    self.df.loc[i, 'trade'] = ''
        return self.df      
        
        # 3번째 함수 생성

    def add_rtn (self):
        #수익률 파생변수 생성
        self.df['return'] = 1
        
        # 판매한 날의 수익률 대입
        
        rtn = 1.0
        buy = 0.0
        sell = 0.0
        
        for i in self.df.index :
            if (self.df.shift(1).loc[i, 'trade'] == '') & (self.df.loc[i,'trade'] == 'buy'):
                buy = self.df.loc[i, self.col]
                print('진입일:', i, '구매가격:', buy)
            
            elif (self.df.shift(1).loc[i, 'trade'] == 'buy') & (self.df.loc[i,'trade'] == ''):
                sell = self.df.loc[i,self.col]
                rtn = (sell - buy) / buy + 1
                self.df.loc[i,'return'] = rtn
                print('판매일:', i, '판매가격:', sell, '수익률:', rtn)
            
            if self.df.loc[i,'trade'] == '':
                buy = 0.0
                sell = 0.0
        
        acc_rtn = 1.0

        for i in self.df.index :
            rtn = self.df.loc[i,'return'] 
            acc_rtn *= rtn
            self.df.loc[i,'acc_rtn'] = acc_rtn
            
        print('누적수익률:', acc_rtn)
        return self.df            
        