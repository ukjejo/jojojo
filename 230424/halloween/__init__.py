# class 선언 Halloween
# 생성자 함수에서 데이터프레임, 시작년도, 종료년도
# self변수를 생성, self.acc_rtn 변수는 1 고정
import pandas as pd

class Halloween:
    def __init__ (self, _df, _start, _end):
        self.df = _df
        self.start = _start
        self.end = _end
        self.acc_rtn = 1
 

# 누적수익률 계산하는 함수        
    def accrtn(self):
        
        if 'Date' in self.df.columns:
            self.df['Date'] = pd.to_datetime(self.df['Date'], format = "%Y-%m-%d")
            self.df.set_index('Date', inplace = True)
        
        # 누적 수익률 변수를 생성
        acc_rtn = 1
        
        for i in range(self.start, self.end):
            
            
            self.buy_mon = str(i) + '-11'                          
            self.sell_mon = str(i+1) + '-04'
            
            self.buy = self.df.loc[self.buy_mon].iloc[0]['Open']
            self.sell = self.df.loc[self.sell_mon].iloc[-1]['Close']
            
            self.rtn = (self.sell - self.buy) / self.buy + 1
            
            self.acc_rtn *= self.rtn
        
        return self.acc_rtn
    
     

# CAGR을 계산하는 함수 (투자기간은 종료년도 - 시작년도)

    def carg(self):
        self.CAGR = (self.acc_rtn ** (1/(self.end - self.start))) - 1
        return (self.CAGR*100)