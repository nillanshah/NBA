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

def get_team_dict():
    d = {
        'ATLANTA HAWKS' : 'ATL',
        'ST. LOUIS HAWKS' : 'SLH',
        'MILWAUKEE HAWKS' : 'MIL',
        'TRI-CITIES BLACKHAWKS' : 'TCB',
        'BOSTON CELTICS' : 'BOS',
        'BROOKLYN NETS' : 'BRK',
        'NEW JERSEY NETS' : 'NJN',
        'CHICAGO BULLS' : 'CHI',
        'CHARLOTTE HORNETS' : 'CHO',
        'CHARLOTTE BOBCATS' : 'CHA',
        'CLEVELAND CAVALIERS' : 'CLE',
        'DALLAS MAVERICKS' : 'DAL',
        'DENVER NUGGETS' : 'DEN',
        'DETROIT PISTONS' : 'DET',
        'FORT WAYNE PISTONS' : 'FWP',
        'GOLDEN STATE WARRIORS' : 'GSW',
        'SAN FRANCISCO WARRIORS' : 'SFW',
        'PHILADELPHIA WARRIORS' : 'PHI',
        'HOUSTON ROCKETS' : 'HOU',
        'INDIANA PACERS' : 'IND',
        'LOS ANGELES CLIPPERS' : 'LAC',
        'SAN DIEGO CLIPPERS' : 'SDC',
        'BUFFALO BRAVES' : 'BUF',
        'LOS ANGELES LAKERS' : 'LAL',
        'MINNEAPOLIS LAKERS' : 'MIN',
        'MEMPHIS GRIZZLIES' : 'MEM',
        'VANCOUVER GRIZZLIES' : 'VAN',
        'MIAMI HEAT' : 'MIA',
        'MILWAUKEE BUCKS' : 'MIL',
        'MINNESOTA TIMBERWOLVES' : 'MIN',
        'NEW ORLEANS PELICANS' : 'NOP',
        'NEW ORLEANS/OKLAHOMA CITY HORNETS' : 'NOK',
        'NEW ORLEANS HORNETS' : 'NOH',
        'NEW YORK KNICKS' : 'NYK',
        'OKLAHOMA CITY THUNDER' : 'OKC',
        'SEATTLE SUPERSONICS' : 'SEA',
        'ORLANDO MAGIC' : 'ORL',
        'PHILADELPHIA 76ERS' : 'PHI',
        'SYRACUSE NATIONALS' : 'SYR',
        'PHOENIX SUNS' : 'PHO',
        'PORTLAND TRAIL BLAZERS' : 'POR',
        'SACRAMENTO KINGS' : 'SAC',
        'KANSAS CITY KINGS' : 'KCK',
        'KANSAS CITY-OMAHA KINGS' : 'KCK',
        'CINCINNATI ROYALS' : 'CIN',
        'ROCHESTER ROYALS' : 'ROR',
        'SAN ANTONIO SPURS' : 'SAS',
        'TORONTO RAPTORS' : 'TOR',
        'UTAH JAZZ' : 'UTA',
        'NEW ORLEANS JAZZ' : 'NOJ',
        'WASHINGTON WIZARDS' : 'WAS',
        'WASHINGTON BULLETS' : 'WAS',
        'CAPITAL BULLETS' : 'CAP',
        'BALTIMORE BULLETS' : 'BAL',
        'CHICAGO ZEPHYRS' : 'CHI',
        'CHICAGO PACKERS' : 'CHI',
        'ANDERSON PACKERS' : 'AND',
        'CHICAGO STAGS' : 'CHI',
        'INDIANAPOLIS OLYMPIANS' : 'IND',
        'SHEBOYGAN RED SKINS' : 'SRS',
        'ST. LOUIS BOMBERS' : 'SLB',
        'WASHINGTON CAPITOLS' : 'WAS',
        'WATERLOO HAWKS' : 'WAT'}
    return d