#!/usr/bin/env python
import pandas as pd
import numpy as np

# read the log file
df = pd.read_table('/bind/data/localizer.txt')
# adjust the times
df['Time'] = df['Time'] - df.iloc[0]['Duration'] - df.iloc[0]['Time']

# remove non condition codes
df = df[~df['Code'].isin(['fix', 'rest', '4', '8', 'checker_flash', 'wait'])]
# convert to seconds
df['Time'] = df['Time']/10000.0

groups = df.groupby(df['Code'])
times = groups['Time'].unique()

destonsets = '/bind/data/onsets'
# save times
for condition in times.index:
	onsets = np.array(times[condition])
	np.savetxt(destonsets, condition + '.txt', onsets[np.newaxis], fmt='%0.2f')


#creates a text file for each code, need to fix path so localizer script can run
#gives local onset times to use in the analysis

