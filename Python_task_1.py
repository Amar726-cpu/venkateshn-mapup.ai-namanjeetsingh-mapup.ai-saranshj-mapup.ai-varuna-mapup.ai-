#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
ds=pd.read_csv(r"C:\Users\USER\Downloads\dataset-1.csv")


# In[2]:


ds.shape


# In[3]:


ds.head()


# In[4]:


ds.tail()


# In[5]:


ds.sample(5)


# In[6]:


ds.isnull().sum()


# In[7]:


ds.columns


# In[8]:


ds['id_1'].unique()


# In[9]:


ds['id_2'].unique()


# In[10]:


ds['route'].unique()


# In[11]:


ds['moto'].unique()


# In[12]:


ds['car'].unique()


# In[13]:


ds['rv'].unique()


# In[14]:


ds['bus'].unique()


# In[15]:


ds['truck'].unique()


# In[16]:


ds1 = pd.DataFrame(ds,columns=sorted(ds['id_2'].unique()),index=sorted(ds['id_1'].unique()))


# In[18]:


ds1.head()


# In[ ]:




