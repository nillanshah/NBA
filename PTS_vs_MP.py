#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:34:27 2020

@author: Nillan
"""
import matplotlib.pyplot as plt
import pandas as pd
from adjustText import adjust_text


df = pd.read_csv("~/Desktop/Programming/NBA/4Q_boxscore.csv")

names = df.PLAYER.unique()
counts = df.PLAYER.value_counts()


def get_count(string):
    temp = counts[[string]]
    return temp[0]

def converter(string):  
    try:
        index = string.index(":")
        
        
        minutes = int(string[:index])
        seconds = int(string[index + 1: ])
        
        dec = round(seconds / 60, 2)
        
        final = minutes + dec
        return final
    except:
        print(string)
    

df.MP = df.MP.apply(lambda x: converter(x))
df["GAMECOUNT"] = df.PLAYER.apply(lambda x: get_count(x))

groups = df.groupby(['PLAYER']).mean()
refined_groups = groups[groups.GAMECOUNT > 4]
refined_groups = refined_groups.dropna()
max(refined_groups.MP)

p = refined_groups

sorted_df = p.sort_values(by = ['PTS'], ascending = False)
sorted_df = sorted_df[sorted_df.MP > 5]
sorted_df = sorted_df[sorted_df.PTS > 3]


plt.scatter(data = sorted_df, x = 'PTS', y = 'FGA')
plt.ylabel('Avg. FGA ')
plt.xlabel('Avg. Points Scored')
plt.title('4th Quarter')

top_n = 7

adjust = []
for player, x,y in zip(sorted_df.index[:top_n], sorted_df.PTS[:top_n], sorted_df.FGA[:top_n]):
    
    adjust.append(plt.text(x, y, player))
    
# =============================================================================
#     plt.annotate(player, # this is the text
#                  (x,y), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(10,10), # distance from text to points (x,y)
#                  ha='center',
#                  arrowprops = {'arrowstyle' : '-'}) # horizontal alignment can be left, right or center
# 
# 
# =============================================================================
adjust_text(adjust, arrowprops=dict(arrowstyle="-", color='black'), ha = 'right')
plt.show()