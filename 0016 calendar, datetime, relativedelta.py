# -*- coding: utf-8 -*-
"""
API를 활용하다보니, 매달 데이터를 전처리 해야 하기에, 편리한 방법을 정리함
"""
##############################
#%%
# 월별 마지막 일 산정
import calendar
k = 2022
month_lastday = [calendar.monthrange(k,i)[1] for i in range(1,13)]
##############################
#%%
from datetime import datetime

today = datetime.today()
now = datetime.now()

print(now.year)          #연
print(now.month)         #월
print(now.day)           #일
print(now.hour)          #시
print(now.minute)        #분
print(now.second)        #초

print(now.strftime('%Y-%m-%d')) #연-월-일
print(now.strftime('%H:%M:%S')) #시:분:초
##############################
#%%
import datetime

print(now+datetime.timedelta(weeks=1))         #1일 후
print(now+datetime.timedelta(weeks=-1))        #1일 전
print(now+datetime.timedelta(hours=5))         #5시간 후
##############################
#%%
from dateutil.relativedelta import relativedelta

print(now+relativedelta(months=1))     #1달 후
print(now+relativedelta(years=1))      #1년 후
##############################
#%%
from datetime import datetime
fix_date = datetime.strptime('2022-04-01 00:30:00', '%Y-%m-%d %H:%M:%S')
print(fix_date)
type(fix_date)
##############################
#%%
# 부등식 비교
# 포맷이 같은 경우
now = datetime.now()
fix_date = datetime.strptime('2022-04-01 00:30:00', '%Y-%m-%d %H:%M:%S')
now<fix_date

# 포맷이 다른 경우(오류 발생)
today_date = now.strftime('%Y-%m-%d')
today_date<fix_date
##############################