#!/usr/bin/python2

import os
import re
import sys
import time
import subprocess 
from dns.resolver import query



trueowncmd = 'sudo cat /etc/trueuserowners'
owners = subprocess.Popen(trueowncmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
truedomcmd = 'sudo cat /etc/trueuserdomains'
domain = subprocess.Popen(truedomcmd, stdout=subprocess.PIPE, shell=True).communicate()[0]

ownList = owners.split('\n')
domList = domain.split('\n')


ownDict = {}
noline = 0
for line in ownList:
    try:
        acct, owner = line.split(': ')
        if owner not in ownDict:
            ownDict[owner] = [acct]
        else:
	    ownDict[owner].append(acct) 
    except ValueError:
        noline += 1	

domDict = {}
noline = 0
for line in domList:
    try:
        dom, acct = line.split(': ')
        if acct not in domDict:
            domDict[acct] = [dom]
        else:
            domDict[acct].append(dom) 
    except ValueError:
        noline += 1	




resDict = {}
for owner in ownDict.keys():
    resDict[owner] = {}
    for acct in ownDict[owner]:
	resDict[owner][acct] = []
	for dom in domDict[acct]:
            resDict[owner][acct].append(dom)


logfile = open('.test',  "a+")
for res in resDict.keys():
    for act in resDict[res].keys():
        for dom in resDict[res][act]:
            logfile.write("|".join([res, act, dom]) + '\n') 
