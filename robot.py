# -*- coding: UTF8 -*-
import urllib.request, json
'''
web = ['https://legacy.gemoney.cz/gen/login',
       'http://microsites.gemoney.cz',
       'https://www.ieservis.cz/',
       'https://www.beneplus.cz/',
       'https://online.gemoney.cz/',
       'https://www.gemoney.cz/lide',
       'https://www.rozvojsnami.cz/',
       'https://www.bankaproneslysici.cz/',
       'https://www.gemoneyauto.cz/',
       'https://www.gemoneyleasing.cz/',
       'https://s.gemoney.cz/']
'''

with open( 'sites.json' ) as sitesData:
    data = json.load(sitesData)
    
  
    
proxy = urllib.request.ProxyHandler({'http':'http://212437054:Santiago2016*06@proxyge:80' ,
                                     'https': 'http://212437054:Santiago2016*06@proxyge:80'})

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
        