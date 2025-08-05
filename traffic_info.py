#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 17:46:24 2025

@author: renakaya
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
#%%
# Parameters
num_sessions = 4182
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 6, 30)
date_range = pd.date_range(start_date, end_date).tolist()

# Possible values
traffic_sources = ['Organic', 'Direct', 'Referral', 'Social', 'Email']
device_types = ['Mobile', 'Desktop', 'Tablet']
countries = ['USA', 'UK', 'Canada', 'Germany', 'India', 'Brazil', 'Australia']
#%%
# Helper functions
def generate_behavior(pageviews):
    if pageviews == 1:
        return 'Bounce' if random.random() < 0.9 else 'Conversion'  # rare conversion on bounce
    else:
        rand = random.random()
        if rand < 0.1:
            return 'Conversion'
        elif rand < 0.5:
            return 'Bounce'
        else:
            return 'Neither'

data = []

for session_id in range(1, num_sessions + 1):
    user_id = random.randint(1, 316)
    date = random.choice(date_range)
    pageviews = np.random.poisson(5) + 1  
    traffic_source = random.choices(traffic_sources, weights=[0.25, 0.15, 0.1, 0.4, 0.1])[0]
    device_type = random.choices(device_types, weights=[0.6, 0.3, 0.1])[0]
    country = random.choices(countries, weights=[0.2, 0.12, 0.08, 0.15, 0.3, 0.08, 0.07])[0]
    behavior = generate_behavior(pageviews)
    session_duration = max(1, int(np.random.normal(45, 100)))  # in seconds, min 10 sec

    data.append([
        f"S{session_id:04d}",
        f"U{user_id:03d}",
        date.date(),
        pageviews,
        traffic_source,
        device_type,
        country,
        behavior,
        session_duration
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'Session ID', 'User ID', 'Date', 'Pageviews',
    'Traffic Source', 'Device Type', 'Country',
    'Behavior', 'Session Duration'
])
path = r'/Users/renakaya/Documents/Work/Analyst_Projects\traffic_info.csv'

df.to_csv(path, index=False)