import sys
from epics import PV
import random
import time

pvValues = [0]*32
pv = [0]*32

#print (pvValues)	# Debbug

def getPvValue(pvName):
    pv = PV(pvName)
    if pv.connected:
        return pv.value
    else:
        return -1

def getRandom():
    return random.uniform(0,100)

def readAIValues():
    #	Read EPS AI Cat Values
    pvValues[0]=pv1.value
    pvValues[1]=pv2.value
    pvValues[2]=pv3.value
    pvValues[3]=pv4.value
    pvValues[4]=pv5.value
    pvValues[5]=pv6.value
    pvValues[6]=pv7.value
    pvValues[7]=pv8.value
    pvValues[8]=pv9.value
    pvValues[9]=pv10.value
    pvValues[10]=pv11.value
    pvValues[11]=pv12.value
    pvValues[12]=pv13.value
    pvValues[13]=pv14.value
    pvValues[14]=pv15.value
    pvValues[15]=pv16.value
    pvValues[16]=pv17.value
    pvValues[17]=pv18.value
    pvValues[18]=pv19.value
    pvValues[19]=pv20.value
    pvValues[20]=pv21.value
    pvValues[21]=pv22.value
    pvValues[22]=pv23.value
    pvValues[23]=pv24.value
    pvValues[24]=pv25.value
    pvValues[25]=pv26.value
    pvValues[26]=pv27.value
    pvValues[27]=pv28.value
    pvValues[28]=pv29.value
    pvValues[29]=pv30.value
    pvValues[30]=pv31.value
    pvValues[31]=pv32.value
    return pvValues

def tamanhoArrayPVs():
    return len(readAIValues())