#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:38:55 2020

@author: Nillan
"""

from basketball_reference_scraper.box_scores import get_box_scores
from basketball_reference_scraper.seasons import get_schedule, get_standings
import pandas as pd

from team_list import *

team_dict = get_team_dict()
team_list = get_team_list()

#get schedule of the season
year = 2020
date = pd.datetime.now() - pd.Timedelta(1, "D")

schedule = get_schedule(year, playoffs = False)
schedule = schedule[schedule.DATE < date]

#go through each match up of the schedule and get the box score
for i in range(0, schedule.shape[0]):
    row = schedule.iloc[i]
    
    date = row.DATE
    team1 = team_dict[row.HOME.upper()]
    team2 = team_dict[row.VISITOR.upper()]
    
    box_score = get_box_scores(date, team1, team2, period = 'Q4')
    
    team1_box_score = box_score[team1]
    team2_box_score = box_score[team2]

    if (i == 0):
        final_box_score = pd.concat([team1_box_score, team2_box_score], ingore_index = True)
    else:
        final_box_score = pd.concat([final_box_score, team1_box_score], ingore_index = True)
        final_box_score = pd.concat([final_box_score, team2_box_score], ingore_index = True)

cleaned_final_box_score = final_box_score[final_box_score.MP != "Did Not Play"] 
cleaned_final_box_score = cleaned_final_box_score[cleaned_final_box_score.MP != "Did Not Dress"] 
cleaned_final_box_score = cleaned_final_box_score[cleaned_final_box_score.MP != "Not With Team"] 

cleaned_final_box_score = cleaned_final_box_score.dropna()

cleaned_final_box_score.to_csv("4Q_boxscore.csv", index = False)