#!/usr/bin/env python


#module imports 
import json
import numpy as np

#sub-{}_task-{}_run-{}_bold.json

fname = '/bind/bids/data/sub-METEST4/func/sub-METEST4_task-localizer_bold.json' #fill in json name wiht respect to the container

#read in
with open(fname) as fp:
	data = json.load(fp) #loads file and parses it so python can understand

print(data) #prints all data
print(data.keys()) #prints headings: keys to dictionaries(key value pairs)

data["SliceTiming"] #reference key: dictname[A]

#save
np.savetxt('/bind/preproc/sub-METEST4/sub-METEST4_task-localizer_stc.txt' , data['SliceTiming'], fmt='%f')

#3dTshift is the afni command that applies slice timing correction
#tpattern @<path to timing files>
#-TR <> repetition time
#-prefix <stc> output name name the same as func nifti 
#<INOUT> input file BOLD file(nifit)
#3dTshift -tpattern @/bind/preproc/IBRAIN002/stc.txt -TR 2 -prefix stc /bind/bids/data/sub-S0318ANN/func/sub-S0318ANN_task-words_run-02_bold.nii
	#output = BRINK(gets actual data) and HEAD files, +orig = in original space data was collected in