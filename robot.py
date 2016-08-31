# -*- coding: UTF8 -*-
import urllib.request, json


with open( 'sites.json' ) as sitesData:
    data = json.load(sitesData)
    
  
    
proxy = urllib.request.ProxyHandler({'http':'http://user:passwd@proxy:8082' ,
                                     'https': 'http://user:passwd@proxy:8082'})

opener = urllib.request.build_opener(proxy)

urllib.request.install_opener(opener)

#str1 = ['GE Money Bank','Vstup','MONETA']

for sites in data:
    conn = urllib.request.urlopen(data[sites[2]])
    result = (conn.read())
    findText = str1[0] in str(result) or str1[1] in str(result) or str1[2] in str(result)
    if findText == True:
        print ('web '+ sites + ' is ok')
        conn = None
    else:
        print ('ERROR: ' + sites)
        conn = None
        
