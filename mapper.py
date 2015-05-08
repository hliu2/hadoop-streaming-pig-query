#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    values = line.split(',')
    
    try:
        custid = int(values[1]) # test whether current line is from transaction   
        print '%d\tA@1' %(custid)       
 
    except ValueError:
       custid = int(values[0])
       name = values[1]
       countrycode = int(values[3])
       if (countrycode == 5): 
           print '%d\tB@%s' %(custid,name) 