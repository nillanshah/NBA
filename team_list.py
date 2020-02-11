#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:10:22 2020

@author: nillan
"""

#avg points allowed
#by team
def get_team_list():
    from basketball_reference_scraper.seasons import get_standings
    
    df = get_standings("2019-01-01")
    
    east = df['EASTERN_CONF']
    west = df['WESTERN_CONF']
    
    east2 = east.TEAM.str.rstrip("*").to_list()
    west2 = west.TEAM.str.rstrip("*").to_list()
    
    for i in range(0, len(west2)):
        east2.append(west2[i])
    
    return east2