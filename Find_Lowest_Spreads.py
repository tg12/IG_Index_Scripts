#IF YOU FOUND THIS USEFUL, Please Donate some Bitcoin .... 1FWt366i5PdrxCC6ydyhD8iywUHQ2C7BWC

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import datetime
import requests
import json
import logging
import sys
import urllib
from time import time, sleep
import random
import time as systime
##################################################
import sys, os
import operator

########################################################################################################################
REAL_OR_NO_REAL = 'https://demo-api.ig.com/gateway/deal'
API_ENDPOINT = "https://demo-api.ig.com/gateway/deal/session"
API_KEY = '***********************' #<-------------Special IG Index API Key, Problem on 23rd Jan
#API_KEY = '***********************'
data = {"identifier":"***********************","password": "***********************"}
########################################################################################################################
########################################################################################################################
########################################################################################################################
# FOR REAL....
########################################################################################################################
########################################################################################################################
########################################################################################################################
# REAL_OR_NO_REAL = 'https://api.ig.com/gateway/deal'
# API_ENDPOINT = "https://api.ig.com/gateway/deal/session"
# API_KEY = '***********************'
# data = {"identifier":"***********************","password": "***********************"}

headers = {'Content-Type':'application/json; charset=utf-8',
        'Accept':'application/json; charset=utf-8',
        'X-IG-API-KEY':API_KEY,
        'Version':'2'
        }

r = requests.post(API_ENDPOINT, data=json.dumps(data), headers=headers)
 
headers_json = dict(r.headers)
CST_token = headers_json["CST"]
print (R"CST : " + CST_token)
x_sec_token = headers_json["X-SECURITY-TOKEN"]
print (R"X-SECURITY-TOKEN : " + x_sec_token)

#GET ACCOUNTS
base_url = REAL_OR_NO_REAL + '/accounts'
authenticated_headers = {'Content-Type':'application/json; charset=utf-8',
        'Accept':'application/json; charset=utf-8',
        'X-IG-API-KEY':API_KEY,
        'CST':CST_token,
        'X-SECURITY-TOKEN':x_sec_token}

auth_r = requests.get(base_url, headers=authenticated_headers)
d = json.loads(auth_r.text)

# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)

for i in d['accounts']:
    if str(i['accountType']) == "SPREADBET":
        print ("Spreadbet Account ID is : " + str(i['accountId']))
        spreadbet_acc_id = str(i['accountId'])

#SET SPREAD BET ACCOUNT AS DEFAULT
base_url = REAL_OR_NO_REAL + '/session'
data = {"accountId":spreadbet_acc_id,"defaultAccount": "True"}
auth_r = requests.put(base_url, data=json.dumps(data), headers=authenticated_headers)

# print(auth_r.status_code)
# print(auth_r.reason)
# print (auth_r.text)
#ERROR about account ID been the same, Ignore! 

###################################################################################
##########################END OF LOGIN CODE########################################
##########################END OF LOGIN CODE########################################
##########################END OF LOGIN CODE########################################
##########################END OF LOGIN CODE########################################
###################################################################################

epic_ids = ["CS.D.AUDUSD.TODAY.IP", "CS.D.EURCHF.TODAY.IP", "CS.D.EURGBP.TODAY.IP", "CS.D.EURJPY.TODAY.IP", "CS.D.EURUSD.TODAY.IP", "CS.D.GBPEUR.TODAY.IP", "CS.D.GBPUSD.TODAY.IP", "CS.D.USDCAD.TODAY.IP", "CS.D.USDCHF.TODAY.IP", "CS.D.USDJPY.TODAY.IP", "CS.D.CADCHF.TODAY.IP", "CS.D.CADJPY.TODAY.IP", "CS.D.CHFJPY.TODAY.IP", "CS.D.EURCAD.TODAY.IP", "CS.D.EURSGD.TODAY.IP", "CS.D.EURZAR.TODAY.IP", "CS.D.GBPCAD.TODAY.IP", "CS.D.GBPCHF.TODAY.IP", "CS.D.GBPJPY.TODAY.IP", "CS.D.GBPSGD.TODAY.IP", "CS.D.GBPZAR.TODAY.IP", "CS.D.MXNJPY.TODAY.IP", "CS.D.NOKJPY.TODAY.IP", "CS.D.PLNJPY.TODAY.IP", "CS.D.SEKJPY.TODAY.IP", "CS.D.SGDJPY.TODAY.IP", "CS.D.USDSGD.TODAY.IP", "CS.D.USDZAR.TODAY.IP", "CS.D.AUDCAD.TODAY.IP", "CS.D.AUDCHF.TODAY.IP", "CS.D.AUDEUR.TODAY.IP", "CS.D.AUDGBP.TODAY.IP", "CS.D.AUDJPY.TODAY.IP", "CS.D.AUDNZD.TODAY.IP", "CS.D.AUDSGD.TODAY.IP", "CS.D.EURAUD.TODAY.IP", "CS.D.TODAY.IP", "CS.D.GBPAUD.TODAY.IP", "CS.D.GBPNZD.TODAY.IP", "CS.D.NZDAUD.TODAY.IP", "CS.D.NZDCAD.TODAY.IP", "CS.D.NZDCHF.TODAY.IP", "CS.D.NZDEUR.TODAY.IP", "CS.D.NZDGBP.TODAY.IP", "CS.D.NZDJPY.TODAY.IP", "CS.D.NZDUSD.TODAY.IP", "CS.D.CHFHUF.TODAY.IP", "CS.D.EURCZK.TODAY.IP", "CS.D.EURHUF.TODAY.IP", "CS.D.EURILS.TODAY.IP", "CS.D.EURMXN.TODAY.IP", "CS.D.EURPLN.TODAY.IP", "CS.D.EURTRY.TODAY.IP", "CS.D.GBPCZK.TODAY.IP", "CS.D.GBPHUF.TODAY.IP", "CS.D.GBPILS.TODAY.IP", "CS.D.GBPMXN.TODAY.IP", "CS.D.GBPPLN.TODAY.IP", "CS.D.GBPTRY.TODAY.IP", "CS.D.TRYJPY.TODAY.IP", "CS.D.USDCZK.TODAY.IP", "CS.D.USDHUF.TODAY.IP", "CS.D.USDILS.TODAY.IP", "CS.D.USDMXN.TODAY.IP", "CS.D.USDPLN.TODAY.IP", "CS.D.USDTRY.TODAY.IP", "CS.D.CADNOK.TODAY.IP", "CS.D.CHFNOK.TODAY.IP", "CS.D.EURDKK.TODAY.IP", "CS.D.EURNOK.TODAY.IP", "CS.D.EURSEK.TODAY.IP", "CS.D.GBPDKK.TODAY.IP", "CS.D.GBPNOK.TODAY.IP", "CS.D.GBPSEK.TODAY.IP", "CS.D.NOKSEK.TODAY.IP", "CS.D.USDDKK.TODAY.IP", "CS.D.USDNOK.TODAY.IP", "CS.D.USDSEK.TODAY.IP", "CS.D.AUDCNH.TODAY.IP", "CS.D.CADCNH.TODAY.IP", "CS.D.CNHJPY.TODAY.IP", "CS.D.BRLJPY.TODAY.IP", "CS.D.GBPINR.TODAY.IP", "CS.D.USDBRL.TODAY.IP", "CS.D.USDIDR.TODAY.IP", "CS.D.USDINR.TODAY.IP", "CS.D.USDKRW.TODAY.IP", "CS.D.USDMYR.TODAY.IP", "CS.D.USDPHP.TODAY.IP", "CS.D.USDTWD.TODAY.IP", "CS.D.EURCNH.TODAY.IP", "CS.D.sp_EURRUB.TODAY.IP", "CS.D.GBPCNH.TODAY.IP", "CS.D.NZDCNH.TODAY.IP", "CS.D.USDCNH.TODAY.IP", "CS.D.sp_USDRUB.TODAY.IP"]

#epic_ids = ['CS.D.USCGC.TODAY.IP', 'CS.D.USCSI.TODAY.IP', 'CS.D.PLAT.TODAY.IP', 'CS.D.PALL.TODAY.IP', 'CS.D.ALUMINIUM.TODAY.IP', 'CS.D.COPPER.TODAY.IP', 'CS.D.LEAD.TODAY.IP', 'CS.D.NICKEL.TODAY.IP', 'CS.D.ZINC.TODAY.IP']

#epic_ids = ['IX.D.FTSE.DAILY.IP', 'KB.D.MID250.DAILY.IP', 'KB.D.TK.DAILY.IP', 'IX.D.FANG.DAILY.IP', 'IX.D.RUSSELL.DAILY.IP', 'IX.D.DOW.DAILY.IP', 'IX.D.SPTRD.DAILY.IP', 'IX.D.CAC.DAILY.IP', 'IX.D.DAX.DAILY.IP', 'IX.D.SMI.DFB.IP', 'IX.D.CSI.DFB.IP', 'IX.D.XINHUA.DFB.IP', 'IX.D.HSCHIN.DFB.IP', 'IX.D.HANGSENG.DAILY.IP', 'IX.D.NIFTY.DFB.IP', 'IX.D.NIKKEI.DAILY.IP', 'TM.D.KLCI.DAILY.IP', 'IX.D.SAF.DAILY.IP', 'TM.D.BOVESPA.DFB.IP', 'KB.D.AERO.DAILY.IP', 'KB.D.BANKS.DAILY.IP', 'KB.D.DRINKS.DAILY.IP', 'KB.D.CHEMS.DAILY.IP', 'KB.D.BUILD.DAILY.IP', 'KB.D.ELECTY.DAILY.IP', 'KB.D.EE.DAILY.IP', 'KB.D.INV.DAILY.IP', 'KB.D.SPECFINAN.DAILY.IP', 'KB.D.PHONES.DAILY.IP', 'KB.D.FOOD.DAILY.IP', 'KB.D.FDR.DAILY.IP', 'KB.D.WATER.DAILY.IP', 'KB.D.RETAIL.DAILY.IP', 'KB.D.GINDU.DAILY.IP', 'KB.D.HEALTH.DAILY.IP', 'KB.D.HSEHLD.DAILY.IP', 'KB.D.ENGINE.DAILY.IP', 'KB.D.BUS.DAILY.IP', 'KB.D.LIFE.DAILY.IP', 'KB.D.MEDIA.DAILY.IP', 'KB.D.MINING.DAILY.IP', 'KB.D.INSURANCE.DAILY.IP', 'KB.D.OIL.DAILY.IP', 'KB.D.OILEQUIP.DAILY.IP', 'KB.D.PGOODS.DAILY.IP', 'KB.D.PHARMA.DAILY.IP', 'KB.D.REAL.DAILY.IP', 'KB.D.SOFT.DAILY.IP', 'KB.D.SUPPORT.DAILY.IP', 'KB.D.ITHARD.DAILY.IP', 'KB.D.TOBACCO.DAILY.IP', 'KB.D.HOTELS.DAILY.IP']

spreads_and_epics = []

for epic_id in epic_ids:
    tmp_lst = []
    base_url = REAL_OR_NO_REAL + '/markets/'+ epic_id
    auth_r = requests.get(base_url, headers=authenticated_headers)
    d = json.loads(auth_r.text)
    # print(auth_r.status_code)
    # print(auth_r.reason)
    # print (auth_r.text)
    # print (epic_id)
    
    try:
        tmp_lst.append(epic_id)

        bid_price = d['snapshot']['bid']
        ask_price = d['snapshot']['offer']
        spread = float(bid_price) - float(ask_price)
        print ("bid : " + str(bid_price))
        print ("ask : " + str(ask_price))
        print ("-------------------------")
        print ("spread : " + str(spread))
        print ("-------------------------")
        tmp_lst.append(spread)
        spreads_and_epics.append(tmp_lst)
        sleep(1)
    except Exception:
        pass
    

sorted_list = sorted(spreads_and_epics, key=operator.itemgetter(1))

for i in range(len(sorted_list)):
    print(sorted_list[i])
                
