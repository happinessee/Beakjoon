#!/usr/bin/env python
# coding: utf-8

# In[3]:


import binance_d
import binance_f
import pandas as pd
import numpy as np
import os
import datetime
import decimal

from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
from binance.client import Client
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.constant.system import RestApiDefine
from binance_f.impl.restapirequestimpl import RestApiRequestImpl
from binance_f.impl.restapiinvoker import call_sync
from binance_f.model.constant import *


binance_api= 'vDiLBxzA2VPlSuBLYXiDF47mScyldTANFIdysXlZYbVtcM9MA7g65F0EKPwG1w9k'
binance_secret= '3gs0sLJ0HnLsHBmcnqEKH46nEklakikZubDefJEbK8wOusHA8XiDtYj0Xw6LrnLY'


# API KEY 설정 (효혁)
request_client = RequestClient(api_key = binance_api, secret_key = binance_secret)
client = Client(binance_api, binance_secret)




#-----------------------------------------------------------------------




# [4] 구현 (펀딩율를 이용한 b값 조정)
#-----------------------------------------------------------------------
# 예제 : b = [{(0.02(예시 펀딩율) - 0.01) * c} + 1]

funding_rate = []
symbol_set = ['DOGEUSDT', 'BNBUSDT', 'ADAUSDT', 'DOTUSDT', 
          'EOSUSDT', 'ETCUSDT', 'LINKUSDT', 'LTCUSDT', 'TRXUSDT']


count0 = 0
b = []
c = -300
initial_entry_usdt = 0.1
need_quantity1 = []   
leverage_set = [50, 75, 75, 75, 75, 75, 75, 75, 75] # 각각 코인의 레버리지를 리스트로 만들었다.

# 넣을 코인의 정보 가져오기---------------------------------------
price_temp = []
for i in symbol_set :
    price_temp.append(request_client.get_symbol_price_ticker(symbol=i))

    
# 코인의 정보에서 가격 정보만 빼서 저장--------------------------------------------------------
length = len(symbol_set)
coin_price = {}        # coin_price['BTCUSDT'] 형식으로 가격을 꺼내쓸 수 있게 만들어뒀다.
coin_price_list = []    
count1 = 0     # 밑의 반복문 횟수 count

for i in range (9) :
    coin_price[symbol_set[i]] = price_temp[i][0].price
    coin_price_list.append(price_temp[i][0].price)
    count1 += 1

for i in range (9) :
        need_quantity1.append(((leverage_set[i] * initial_entry_usdt) / coin_price_list[i]))

print(coin_price_list)

# 펀딩비
for i in symbol_set :
        
    funding_rate.append(request_client.get_funding_rate(symbol=i, limit = 1))
    b.append(((funding_rate[count0][0].fundingRate - 0.0001) * c) + 1)    # 해당 공식을 적용시켜준다.
    count0 += 1


print(b)
print(need_quantity1)
#-----------------------------------------------------------------------
# 롱a * b * 2^(n-1), 
# 숏 a * b * 2 * 2^(n-1) 이다. [a = -500]



def long_general(b, a = -500, n = 3) :
    temp = []
    for i in range (n) :
        temp.insert(i, a * b * (2 ** (i)))
    return temp

def short_general(b, a = -500, n = 3) :
    temp = []
    for i in range (n) :
        temp.insert(i, a * b * (2 ** (i)))
    return temp



# In[ ]:





# In[ ]:


# amount = [0, 2, 0, 1, 1, 2, 2, 3, 0]
# #symbol_set = ['DOGEUSDT', 'BNBUSDT', 'ADAUSDT', 'DOTUSDT', 'EOSUSDT', 'ETCUSDT', 'LINKUSDT', 'LTCUSDT', 'TRXUSDT']
# for i in range(9) :
#     print(need_quantity1[i])
#     if (amount[i] == 0) :
#         need_quantity1[i] = round(need_quantity1[i])
#     else :
#         need_quantity1[i] = round(need_quantity1[i],amount[i])
#     print(need_quantity1[i])
    
# # 나는 leverage의 최대치가 가능한 높은 순으로 코인을 넣었다.
# #
# b = client.futures_create_order(symbol=symbol_set[0], side='BUY', positionSide = 'LONG', type='MARKET', quantity=need_quantity1[0])
# c = client.futures_create_order(symbol=symbol_set[0], side='SELL', positionSide = 'SHORT', type='MARKET', quantity=need_quantity1[0])
# b = client.futures_create_order(symbol=symbol_set[1], side='BUY', positionSide = 'LONG', type='MARKET', quantity= need_quantity1[1])
# c = client.futures_create_order(symbol=symbol_set[1], side='SELL', positionSide = 'SHORT', type='MARKET', quantity= need_quantity1[1])
# b = client.futures_create_order(symbol=symbol_set[2], side='BUY', positionSide = 'LONG', type='MARKET', quantity=need_quantity1[2])
# c = client.futures_create_order(symbol=symbol_set[2], side='SELL', positionSide = 'SHORT', type='MARKET', quantity=need_quantity1[2])

# b = client.futures_create_order(symbol=symbol_set[4], side='BUY', positionSide = 'LONG', type='MARKET', quantity=need_quantity1[3])
# c = client.futures_create_order(symbol=symbol_set[4], side='SELL', positionSide = 'SHORT', type='MARKET', quantity=need_quantity1[3])
# b = client.futures_create_order(symbol=symbol_set[5], side='BUY', positionSide = 'LONG', type='MARKET', quantity=need_quantity1[4])
# c = client.futures_create_order(symbol=symbol_set[5], side='SELL', positionSide = 'SHORT', type='MARKET', quantity=need_quantity1[4])
# b = client.futures_create_order(symbol=symbol_set[6], side='BUY', positionSide = 'LONG', type='MARKET', quantity=need_quantity1[5])
# c = client.futures_create_order(symbol=symbol_set[6], side='SELL', positionSide = 'SHORT', type='MARKET', quantity=need_quantity1[5])
# b = client.futures_create_order(symbol=symbol_set[7], side='BUY', positionSide = 'LONG', type='MARKET', quantity=need_quantity1[6])
# c = client.futures_create_order(symbol=symbol_set[7], side='SELL', positionSide = 'SHORT', type='MARKET', quantity=need_quantity1[6])
# b = client.futures_create_order(symbol=symbol_set[8], side='BUY', positionSide = 'LONG', type='MARKET', quantity=need_quantity1[7])
# c = client.futures_create_order(symbol=symbol_set[8], side='SELL', positionSide = 'SHORT', type='MARKET', quantity=need_quantity1[7])
# b = client.futures_create_order(symbol=symbol_set[9], side='BUY', positionSide = 'LONG', type='MARKET', quantity=need_quantity1[8])
# c = client.futures_create_order(symbol=symbol_set[9], side='SELL', positionSide = 'SHORT', type='MARKET', quantity=need_quantity1[8])


# In[ ]:


# 우리가 물타기를 위해 설정한 변수 값 --------------
b = []
n = 3
a = -500
initial_entry_usdt = 0.1
c= -300
# --------------------------------------------------


# 각 코인에 맞는 precision를 일일이 구했다.
amount = [0, 2, 0, 1, 1, 2, 2, 3, 0]
#symbol_set = ['DOGEUSDT', 'BNBUSDT', 'ADAUSDT', 'DOTUSDT', 'EOSUSDT', 'ETCUSDT', 'LINKUSDT', 'LTCUSDT', 'TRXUSDT']
for i in range(9) :
    print(need_quantity1[i])
    if (amount[i] == 0) :
        need_quantity1[i] = round(need_quantity1[i])
    else :
        need_quantity1[i] = round(need_quantity1[i],amount[i])
    print(need_quantity1[i])
    
# 그러나, 강제 반올림을 시켜주면서 가격이 맞지 않는 문제 (총 가치가 5.0usdt가 되지 않는 문제 발생)
    
#[1] 구현
# -----------------------------------------------------------------------------------
symbol_set = ['DOGEUSDT', 'BNBUSDT', 'ADAUSDT', 'DOTUSDT', 
          'EOSUSDT', 'ETCUSDT', 'LINKUSDT', 'LTCUSDT', 'TRXUSDT']    # 나는 leverage의 최대치가 가능한 높은 순으로 코인을 넣었다.
leverage_set = [50, 75, 75, 75, 75, 75, 75, 75, 75] # 각각 코인의 레버리지를 리스트로 만들었다.

for i in range(length) :
    client.futures_change_leverage(symbol = symbol_set[i], leverage = leverage_set[i])
    
    client.futures_create_order(symbol=symbol_set[i], side='BUY', positionSide = 'LONG', type='MARKET', quantity=need_quantity1[i])
    client.futures_create_order(symbol=symbol_set[i], side='SELL', positionSide = 'SHORT', type='MARKET', quantity=need_quantity1[i])

# order[0 ~ 19] 까지의 orderList가 만들어졌다.

#-----------------------------------------------------------------------------------


# [2] 구현 (이 부분부터 반복문 필요)


while(True) :
    count = 0    # pnl 구할 때 사용
    count0 = 0   # funding_rate 구할 때 사용
    storage = 0
    total_pnl_temp = []
    total_amount = []
    # 내 계좌의 포지션
    mode_Choice = request_client.get_position_v2();
    
    # 각자 다른 펀딩비를 가져온다.
    for i in symbol_set :
        
        funding_rate.append(request_client.get_funding_rate(symbol=i, limit = 1))
        b.append(((funding_rate[count0][0].fundingRate - 0.0001) * c) + 1)    # 해당 공식을 적용시켜준다.
        count0 += 1


    # pnl을 배열로 가져온다.
    for i in (mode_Choice) :
        for j in symbol_set :
            if (i.symbol == j) :
                total_pnl_temp.insert(count, i.unrealizedProfit)
            count += 1

    total_pnl_length = len(total_pnl_temp)
    total_pnl = []

    # 양 포지션 (long, short)의 pnl을 더해 total_pnl로 만듬
    for i in range (total_pnl_length) : # length 20
        if (i % 2 == 0) :
            total_pnl.append(total_pnl_temp[i] + total_pnl_temp[i+1])




    # 넣을 코인의 정보 가져오기---------------------------------------
    price_temp = []
    for i in symbol_set :
        price_temp.append(request_client.get_symbol_price_ticker(symbol=i))


    # 코인의 정보에서 가격 정보만 빼서 저장--------------------------------------------------------
    length = len(symbol_set)
    coin_price = {}        # coin_price['BTCUSDT'] 형식으로 가격을 꺼내쓸 수 있게 만들어뒀다.
    coin_price_list = []

    count1 = 0     # 밑의 반복문 횟수 count
    for i in range (length) :
        coin_price[symbol_set[i]] = price_temp[i][0].price
        coin_price_list.append(price_temp[i][0].price)
        count1 += 1



    # 우리가 넣어야 하는 quantity 양
    need_quantity = []   
    
    

    for i in range (length) :
        need_quantity.append(((leverage_set[i] * initial_entry_usdt) / coin_price_list[i]))
        
    for i in range (length) :
        need_quantity[i] = float(round(need_quantity[i], amount[i]))


    # 우리가 계산할 때 사용할 ROE
    ROE = []
    for i in range (total_pnl_length) :    # length 20

        ROE.insert(i, (total_pnl_temp[i] / initial_entry_usdt) * 100)




    # 물타기, 불타기를 할 때 이용할 ROE 설정 값
    long_roe_value = []
    short_roe_value = []
    
    # 코인마다 다른 펀딩비를 사용하므로 2차원 배열을 이용해준다.
    for i in range (length) :  # length 10
    
        long_roe_temp = long_general(b= b[i])
        long_roe_value.append(long_roe_temp)
        short_roe_temp = short_general(b = b[i])
        short_roe_value.append(short_roe_temp)
    

    count_watering = []
    count_firing = []

    for i in range (length) :
        count_watering.append(0)
        count_firing.append(0)



# 각 주문의 최소 명목 가치는 5 USDT의 임계 값 이상이어야합니다. 
# 주문의 명목 가치가 설정된 임계 값 (5 USDT)보다 작은 경우 주문이 거부됩니다.


# 주문 알고리즘

    for i in range (9) :
        # 롱 포지션이 손해 (long 포지션이 (-)%)
        if (ROE[2 * i] <= long_roe_value[i][count_watering[i]]) :

            if (count_watering[i] >= 1 and count_firing[i] < n) :
                client.futures_create_order(symbol=symbol_set[i], side='SELL', positionSide = 'SHORT', type='MARKET', quantity=need_quantity[i])
                count_firing[i] += 1

            if (count_watering[i] < n) :
                client.futures_create_order(symbol=symbol_set[i], side='BUY', positionSide = 'LONG', type='MARKET', quantity=need_quantity[i])
                count_watering[i] += 1

        # 숏 포지션이 손해 
        elif (ROE[2 * i + 1] <= short_roe_value[i][count_watering[i]]) :

            if (count_watering[i] >= 1 and count_firing[i] < n) :
                client.futures_create_order(symbol=symbol_set[i], side='BUY', positionSide = 'LONG', type='MARKET', quantity=need_quantity[i])
                count_firing[i] += 1

            if (count_watering[i] < n) :
                client.futures_create_order(symbol=symbol_set[i], side='SELL', positionSide = 'SHORT', type='MARKET', quantity=need_quantity[i])
                count_watering[i] += 1

        # 총 pnl이 initial_entry_usdt(0.1) 보다 커진다면 모든 포지션 종료 후 다시 재진입
        if (total_pnl[i] > initial_entry_usdt) :
            for j in mode_Choice :
                for k in symbol_set :
                    if (j.symbol == k) :
                        total_amount.append(j.positionAmt)
                        
            client.futures_create_order(symbol=symbol_set[i], side='SELL', positionSide = 'LONG', type='MARKET', quantity=total_amount[2*i])
            client.futures_create_order(symbol=symbol_set[i], side='BUY', positionSide = 'SHORT', type='MARKET', quantity=total_amount[2*i + 1])
                        
            # 재진입
            client.futures_create_order(symbol=symbol_set[i], side='BUY', positionSide = 'LONG', type='MARKET', quantity=need_quantity[i])
            client.futures_create_order(symbol=symbol_set[i], side='SELL', positionSide = 'SHORT', type='MARKET', quantity=need_quantity[i])
            


    


# 
# # 현재 코인마다 미실현 손익. 청산가격, 레버리지, 타입(교차, 격리) 등의 정보를 알려준다.
# 
# # position이 가지고 있는 정보------------------------------------------------------
# # class Position:
# 
# #     def __init__(self):
# #         self.entryPrice = 0.0
# #         self.isAutoAddMargin = False
# #         self.leverage = 0.0
# #         self.maxNotionalValue = 0.0
# #         self.liquidationPrice = 0.0
# #         self.markPrice = 0.0
# #         self.positionAmt = 0.0
# #         self.symbol = ""
# #         self.unrealizedProfit = 0.0
# #         self.marginType = ""
# #         self.isolatedMargin = 0.0
# #         self.positionSide = ""
# # ---------------------------------------------------------------------------------
# 
# 
# # # position을 사용하는 실제 예제
# 
# 
# # for i in mode_Choice :
# #     print(i.symbol)                # coin의 유형
# #     print(i.leverage)              # coin의 레버리지
# #     print(i.unrealizedProfit)      # coin의 미실현 손익
# 
# # 각 주문의 최소 명목 가치는 5 USDT의 임계 값 이상이어야합니다. 
# # 주문의 명목 가치가 설정된 임계 값 (5 USDT)보다 작은 경우 주문이 거부됩니다.
# # order = client.futures_create_order(symbol='EOSUSDT',side = 'BUY', positionSide = 'LONG', type='MARKET', quantity = initial_entry_usdt * leverage[]
# # order = client.futures_create_order(symbol='EOSUSDT',side = 'SELL', positionSide = 'SHORT', type='MARKET', quantity = 1)
# 
# 
# # side = SELL, positionSide = SHORT 숏일때 사는거
# 
# #print(client.futures_account_balance())
# 

# In[ ]:


need_quantity1 = []   

for i in range (length) :
        need_quantity1.append(((leverage_set[i] * initial_entry_usdt) / coin_price_list[i]))

for i in range (10) :
    need_quantity1[i] = float(round(need_quantity1[i], 5))
    
print(need_quantity1)


# 

# In[ ]:




