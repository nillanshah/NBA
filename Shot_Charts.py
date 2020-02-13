#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:43:11 2020

@author: Nillan
"""

from basketball_reference_scraper.shot_charts import get_shot_chart
from basketball_reference_scraper.pbp import get_pbp


d = get_shot_chart('2019-12-28', 'TOR', 'BOS')

pbp = get_pbp('2019-12-28', 'TOR', 'BOS')

# when joel embiid is making more threes, how does bill simmons do
    #by qtr?
