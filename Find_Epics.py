#!/usr/bin/env python3

import requests
import simplejson as json
import time

url = 'https://api.ig.com/gateway/deal'
s = requests.Session()
s.headers = { 'Content-Type' : 'application/json; charset=UTF-8',
              'Accept' : 'application/json; charset=UTF-8',
              'VERSION' : '2',
              'X-IG-API-KEY' : '*****************'
              }
data = { 'identifier' : '*****************',
         'password' : '*****************'
         }
r = s.post(url + '/session', json=data)

s.headers.update({'X-SECURITY-TOKEN': r.headers['X-SECURITY-TOKEN'],
                  'CST': r.headers['CST'],
                  'VERSION' : '1'})

                  
# r = s.get(url + '/markets?searchTerm=FTSE')
# # print(r.status_code)
# # print(r.reason)
# # print (r.text)
# for epic_id in r.json()['markets'] :
 # print (epic_id['epic'])   

                 
def exploreNode(nodeID, liste) :
    r = s.get(url + '/marketnavigation/' + nodeID)
    # print(r.status_code)
    # print(r.reason)
    # print (r.text)
    if isinstance( r.json()['nodes'], list ) :
        for node in r.json()['nodes'] :
            time.sleep(1)
            exploreNode(node['id'], liste)
            print(node['name'])
    if isinstance( r.json()['markets'], list ) :
        for market in r.json()['markets'] :
            #print(market['epic'])
            if "DFB" in str(market['epic']):
                liste.append(market['epic'])
                #print(market['epic'])
            if "TODAY" in str(market['epic']):
                liste.append(market['epic'])
                #print(market['epic'])
            if "DAILY" in str(market['epic']):
                liste.append(market['epic'])
                #print(market['epic'])
        

types = { 'LSE':'107565'}

# 93262
# Indices
# #################
# 165333
# Forex
# #################
# 93237
# Commodities Metals Energies
# #################
# 740446
# Cryptocurrency
# #################
# 94005
# Bonds and Moneymarket
# #################
# 150222
# ETFs, ETCs & Trackers
# #################
# 107565
# Shares - UK
# #################
# 100801
# Shares - UK International (IOB)
# #################
# 133682
# Shares - LSE (UK)
# #################
# 377740
# Shares - US (All Sessions)
# 105486
# Shares - US
# 93846
# Shares - Australia
# 93406
# Shares - Austria
# 93475
# Shares - Belgium
# 93395
# Shares - Canada
# 93398
# Shares - Denmark
# 93566
# Shares - Finland
# 93629
# Shares - France
# 93843
# Shares - Germany
# 93170
# Shares - Greece
# 93357
# Shares - Hong Kong
# 100380
# Shares - Ireland (ISEQ)
# 100307
# Shares - Ireland (LSE)
# 105809
# Shares - Netherlands
# 93411
# Shares - Norway
# 93563
# Shares - Portugal
# 93381
# Shares - Singapore
# 93360
# Shares - South Africa
# 93429
# Shares - Sweden
# 93401
# Shares - Switzerland
# 656351
# Digital 100s: 2 Hour FX
# 656381
# Digital 100s: 2 Hourlies
# 656390
# Digital 100s: 20 Min Markets
# 656120
# Digital 100s: 5 Min Markets
# 656118
# Digital 100s: FX
# 656416
# Digital 100s: Hourlies
# 656119
# Digital 100s: Indices
# 656407
# Digital 100s: Specials
# 656128
# Digital 100s:Commodities
# 110169
# Options (Australian, Cash)
# 302518
# Options (Eu Stocks 50)
# 157735
# Options (France 40)
# 125257
# Options (FTSE)
# 110184
# Options (Germany)
# 157943
# Options (Italy 40)
# 268825
# Options (Netherlands 25)
# 157738
# Options (Spain 35)
# 399997
# Options (Sweden 30)
# 346003
# Options (US 500)
# 125267
# Options (Wall St)
# 322274
# Options on FX Majors
# 166251
# Options on Metals, Energies
# 10891422
# Weekend Indices
          
liste = []
for t in types.keys() :
    exploreNode( types[t], liste)

r = s.delete(url + '/session')

print(liste)
