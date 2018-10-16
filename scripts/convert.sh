#!/bin/bash

### INSERT YOUR CODE BELOW ###
#create example .json files
#dcm2bids_helper -d raw/IBRAIN002 -o bids

#convert dicom files
dcm2bids -d /bind/raw/$1 -p $1 -c /bind/scripts/dcm2bids.json -o /bind/bids/data

### DO NOT MODIFY THE LINES BELOW ###
uname -a > info_host.txt
/usr/bin/env > info_env.txt
ls / > info_fs.txt
mount |grep ^/dev/ | grep -v /etc > info_volumes.txt
