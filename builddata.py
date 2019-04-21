#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[27]:


numFiles = 3
numScan = 20

## for each location file
for i in range(1,numFiles+1):
    dirPath = "location_" + str(i) + "_data/"
    for j in range(1,numScan+1):
        subPath = "db%s.csv" % j
        path = dirPath + subPath
        ## "file_{}.dat".format(i)
        data = pd.read_csv(path)
        
        new = data[['MAC Address','RSSI']]
        new = new.set_index('MAC Address')
        if j == 1:
            if i == 1:
                ## using top 6 initial signal strengths (can be changed for specific case)
                ## these 6 will refer to 6 highest potential APs
                ref = new[0:6]
                reflist = ref.index.values.tolist()
                base = pd.DataFrame(index=ref.index)
            fulldf = base
        new = new['RSSI'].to_dict()
        applist = []
        for k in reflist:
            toapp = 0
            for x,y in new.items():
                if x == k:
                    toapp = y
            applist.append(toapp)
        add = np.asarray(applist)
        fulldf[('RSSI%d' % j)] = add
    ## fulldf now refers to all rssi values sorted by scan and AP(MAC Address) for 1 vector
    ## We must now transpose each df, find the average RSSI and append the resulting vector
    ## to our final data df, then export as a csv
    fulldf = fulldf.T
    ## replace all zero values with nan
    fulldf.replace(0, np.nan, inplace= True)
    print(fulldf.head())
    ## create the vector which will be fed to NN
    vec = []
    
    for column in fulldf:
        avg = fulldf[column].mean()
        vec.append(avg)
    vec.append(i)
    print(vec)


# In[ ]:




