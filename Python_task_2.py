#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


ds=pd.read_csv(r"C:\Users\USER\Downloads\dataset-3.csv")


# In[3]:


ds.head()


# In[4]:


ds.tail()


# In[5]:


ds.shape


# In[6]:


ds.isnull().sum()


# In[7]:


ds.columns


# In[8]:


ds['id_start'].unique()


# In[9]:


ds['id_end'].unique()


# In[10]:


ds['distance'].unique()


# In[11]:


ds=pd.DataFrame(ds,columns=sorted(ds['id_start'].unique()),index=sorted(ds['id_start'].unique()))


# In[12]:


ds.head()


# In[ ]:




