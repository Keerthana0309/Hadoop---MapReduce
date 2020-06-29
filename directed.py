import os
import sys 

from operator import itemgetter

path = '/home/nataraka/directed/part-r-00000'
doc=open('/home/nataraka/directed/part-r-00000')

d1={}
d2={}

for line in doc:
    wd=line.split()
    
    if len(wd)!=0:
        
        k=str(wd[1])
        
        k2=wd[0]
        
        z=k.split('#')
        
        k1=z[1]
        
        d1.update({k2:int(k1)})
        d2.update({z[2]:z[0]})

z1=sorted(d1.items(), key=itemgetter(1))

print('Node with minimum connectivity is',str(z1[0][0]),'with',z1[0][1])
print('Node with maximum connectivity is',str(z1[-1][0]),'with',z1[-1][1])

for a,b in d2.items():
    if a == z1[-1][0]:
       
        print('The longest adjecency list is:-' + ' ' +str(b) + ' ' +'of node'+ ' ' +str(a))
        