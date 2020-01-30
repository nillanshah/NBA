#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:32:45 2020

@author: Nillan
"""

from basketball_reference_scraper.seasons import get_schedule, get_standings
from datetime import timedelta
import pandas as pd
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc

start_year = 2000
end_year = 2013
final_dict = {}


#year = 2010

for year in range(start_year, end_year, 1):
    all_results = get_schedule(year, playoffs=False)
    teams = all_results.HOME.unique().tolist()
    
    date = str(year) + '-06-06'
    standings = get_standings(date=date)
    combined_standings = pd.concat([standings['EASTERN_CONF'], standings['WESTERN_CONF']])
    combined_standings.TEAM = combined_standings.TEAM.str.rstrip('*')

    final_dict[year] = {}    
    
    for team in teams:
    #team = 'Miami Heat'
    
        heat_home = all_results[all_results.HOME.eq(team)]
        heat_away = all_results[all_results.VISITOR.eq(team)]
        
        heat = all_results[(all_results['HOME']==team) | (all_results['VISITOR']==team)]
        
        num_games = heat.shape[0]
        
        heat["GAME_BEFORE"] = [False] * num_games
        
        for i in range (0, num_games - 1):
            if (heat.DATE.iloc[i] + timedelta(days = 1) == heat.DATE.iloc[i + 1]):
                heat.GAME_BEFORE.iloc[i] = True
                heat.GAME_BEFORE.iloc[i + 1] = True
        
        heat_b2b = heat[(heat['GAME_BEFORE'] == True)]
        
        heat_b2b_away = heat_b2b[(heat['VISITOR'] == team)]
        heat_b2b_home = heat_b2b[(heat['HOME'] == team)]
        
        num_b2b = heat_b2b.shape[0]
        
        #new df, same structure
        b2b_away = pd.DataFrame(data=None, columns=heat_b2b.columns)
        
        #go thru home, look to see if there is a date + 1 in away, if there is get that data in b2b away
        num_b2b_home = heat_b2b_home.shape[0]
        
        for j in range(0, num_b2b_home):
        
            date = heat_b2b_home.DATE.iloc[j]
            date_pp = pd.Timestamp(date + timedelta(days = 1))
            
            if (date_pp in heat_b2b_away.DATE.tolist()):
                temp = pd.DataFrame(heat_b2b_away[heat_b2b_away['DATE'] == date_pp])
                b2b_away = pd.concat([b2b_away, temp])
                
        num_b2b_away = b2b_away.shape[0]
        num_b2b_away_wins = 0
        
        for i in range(0, num_b2b_away):
            vis_pts = b2b_away.VISITOR_PTS.iloc[i]
            home_pts = b2b_away.HOME_PTS.iloc[i]
            
            if (vis_pts > home_pts):
                num_b2b_away_wins += 1
        if (num_b2b_away != 0):
            b2b_away_pct = round(num_b2b_away_wins / num_b2b_away, 2)
        else:
            b2b_away_pct = 0 #0 or null?
            
        temp = combined_standings[combined_standings.TEAM.eq(team)]
        WL_perc = round(float(temp['W/L%']), 2)
        difference = round(WL_perc - b2b_away_pct, 2)
        final_dict[year][team] = {'b2b_away_pct' : b2b_away_pct,
                  'b2b_away_wins' : num_b2b_away_wins,
                  'b2b_away_games' : num_b2b_away,
                  'season_WL_pct' : WL_perc,
                  'diff' : difference}

temp = combined_standings[combined_standings.TEAM.eq('Miami Heat')]
temp2 = round(float(temp['W/L%']), 2)
#figure out how to store data
#you need to loops, for team then for year

#b2b_away.append(pd.DataFrame(heat_b2b_away[heat_b2b_away['DATE'] == date_pp]))
        
