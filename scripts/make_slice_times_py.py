#!/usr/bin/env python

# module imports
import json
import numpy as np

fname = '/bind/bids/data/sub-METEST4/func/sub-METEST4_task-localizer_bold.json'

# read
with open(fname) as fp:
  data = json.load(fp)

# save
np.savetxt('/bind/preproc/sub-METEST4/sub-METEST4_task-localizer_stc.txt', data['SliceTiming'], fmt='%f')