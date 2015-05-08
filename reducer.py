#!/usr/bin/env python
from operator import itemgetter
import sys


current_key = None  
key = None 
numoftrans= 0
fromTrans = False
fromCust = False 
flag = None 
for line in sys.stdin:
    line = line.strip()
    current_key, value = line.split('\t',1)
    flag, value = value.split('@')    
    if (key == current_key):
        if (flag == 'A'):
            fromTrans = True    
            numoftrans += int(value)
        if (flag == 'B'):
            fromCust = True  
            name = value
    else:
        if (fromCust and fromTrans):
            print '%s\t%s,%d' %(key,name,numoftrans)
        fromTrans = False
        fromCust = False  
        key = current_key 

        if (flag == 'A'):
            fromTrans == True
            numoftrans = int(value)
            name = None  
        else:
            fromCust = True
            name = value 
 
                        
if (fromCust and fromTrans):
    print '%s\t%s,%d' %(current_key,name,numoftrans)