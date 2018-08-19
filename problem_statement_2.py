
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[31]:


df = pd.read_csv('https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv')
df.head(2)


# In[4]:


df1 = pd.read_csv('https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv')
df1.head(2)


# # 1. META DATA FROM THE DATAFRAMES

# In[6]:


df.info()


# In[7]:


df1.info()


# # 2. Row names from the dataframes

# In[11]:


np.array(list(df.index))


# In[12]:


np.array(list(df1.index))


# # 3. Change the column name 

# In[32]:


# changing the column name of df from indictor to indicator_id
df.rename(columns={'Indicator':'Indicator_Id'})


# In[18]:


df.head(2)


# # 4. Permenantly change the column name

# In[33]:


df.rename(columns={'Indicator':'Indicator_Id'},inplace=True)
df.head(5)


# # 5. Change the names of multiple columns

# In[34]:


# performing changes in the df
# PUBLISH STATES -> Publish States
# WHO region     -> WHO Region

df.rename(columns={'PUBLISH STATES':'Publish States','WHO region':'WHO Region'},inplace=True)
df.head(5)


# # 6. Arrange values of a column in ascending order

# In[40]:


# arranging the Year column values in ascending order
df.sort_values('Year',inplace=True)
df


# # 7. Arrange multiple column values in ascending order.

# In[42]:


df.sort_values(by=['Display Value','Numeric'],inplace=True)
df

