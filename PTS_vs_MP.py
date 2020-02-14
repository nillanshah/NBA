#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:34:27 2020

@author: Nillan
"""
import pandas as pd

df = pd.read_csv("~/Desktop/Programming/NBA/4Q_boxscore.csv")

names = df.PLAYER.unique()
counts = df.PLAYER.value_counts()

counts[['James Harden']][0]

def get_count(string):
    temp = counts[[string]]
    return temp[0]

def converter(string):    
    index = string.index(":")
    
    minutes = int(string[:index])
    seconds = int(string[index + 1: ])
    
    dec = round(seconds / 60, 2)
    
    final = minutes + dec
    return final

df.MP = df.MP.apply(lambda x: converter(x))
df["GAMECOUNT"] = df.PLAYER.apply(lambda x: get_count(x))

groups = df.groupby(['PLAYER']).mean()
refined_groups = groups[groups.GAMECOUNT > 4]
max(refined_groups.MP)

refined_groups.plot(kind = "scatter", x = "MP", y = "PTS")
