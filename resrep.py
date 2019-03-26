#!/usr/bin/python2

import os
import re
import sys
import time
import subprocess 
from dns.resolver import query

epoch = str(time.time()).split('.')[0]


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



out = open('out', "a+")
out.write('henlo\n')
out.close()
out = open('out', "a+")
out.write('henlo\n')
out.close()
out = open('out', "a+")
out.write('henlo\n')
out.close()

resDict = {}
for owner in ownDict.keys():
    resDict[owner] = {}
    for acct in ownDict[owner]:
	resDict[owner][acct] = []
	for dom in domDict[acct]:
            resDict[owner][acct].append(dom)

outList = ['', '', '', '', '']
for res in resDict.keys():
    outList[0] = str(res)
    for act in resDict[res].keys():
	outList[1] = str(act)
        for dom in resDict[res][act]:
	    outList[2] = str(dom)
            for rec in ['A', 'NS', 'SOA']:
		outList[3] = str(rec)
                try:
                    for rep in query(dom, rec):
			outList[4] = str(rep)
			outFile = open(str(epoch), "a+")
			outFile.write(str("|".join(outList) + '\n'))
			outFile.close()
                except:
                    nf = True
