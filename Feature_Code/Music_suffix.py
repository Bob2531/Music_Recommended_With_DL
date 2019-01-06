#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os
from os import listdir


# In[11]:


def suffixList():
    path = '/media/bob/LocalDisk/CloudMusic'
    music_names = listdir(path)

    suffix = []
    for name in music_names: 
        suff = os.path.splitext(name)[-1]
        if suff in suffix: 
            pass 
        else: 
            suffix.append(suff)
    suffix.remove('')
    suffix.remove('.ncm')
    suffix.remove('.jpg')
    return suffix
    #print(suffix)


# choose mp3, flac, wav, ape
