#!/usr/bin/env python
# coding: utf-8

# In[5]:


print("Name :")
print("We will learn how to perform group by operation and count number of Missions as per the company, and plot a bar graph out of it")
print("We will learn how to perform group by operation and count the status of the Missions, and plot a pie chart out of it")
print("We will learn how to search the number of active rockets, and perform group by operation and count number of active rockets as per the company and plot a bar graph out of it")


# In[1]:


import  numpy as np
import pandas as pd 
import matplotlib .pyplot as plt

dataframe = pd.read_csv("space_Corrected.csv")
df=dataframe.dropna()

df


# In[8]:


#Activity-1
#Find total number of missions by each company, and plot a bar graph on it
#First group by Company Name and count Status Mission and create a new dataframe out of it
group_by_name = df.groupby('Company Name')['Status Mission'].count().reset_index()
print(group_by_name)
fig = plt.subplots(figsize=(16,8))
plt.title('Total Missions (Since 1957)', fontsize=20)
plt.xlabel('Company Name', fontsize=16)
plt.ylabel('Mission Counts', fontsize=16)
plt.xticks(rotation='vertical')

label = group_by_name['Company Name']
value = group_by_name['Status Mission']
plt.bar(label, value,width=0.4, color=('red', 'blue', 'green', 'purple', 'orange'))


# In[11]:


#Activity-2
#Find out the percentage of rocket Success, Failure, Partial Failure, and Prelaunch Failure. And plot a pie chart
group_by_status = df.groupby('Status Mission')['Status Rocket'].count().reset_index()
print(group_by_status)
value = group_by_status['Status Rocket']
label = group_by_status['Status Mission']
plt.pie(value, labels=label, autopct='%0.1f%%', radius=2)
pie.show()


# In[15]:


#Activity-3
# Find the number of Active Rockets as per the company and plot a bar grap of it

#First search where Status Rocket column value is equal to StatusActive
search_StatusActive= df.loc[df['Status Rocket'] == 'Status Active']

#Then group by Company Name and count Status Rocket and create a new dataframe out of it
group_by_status = search_StatusActive.groupby('Company Name')['Status Rocket'].count().reset_index()
print(group_by_status)
fig = plt.subplots(figsize=(16,8))
plt.xlabel('Company Name')
plt.xticks(rotation='vertical')
plt.ylabel("Number Of Active Rockets")

#Then get all the Company Name and Status Rocket count and use these 2 values to plot a bar graph
label = group_by_status['Company Name']
value = group_by_status['Status Rocket']

plt.bar(label, value,width=0.4, color=('red', 'blue', 'green', 'purple', 'orange'))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




