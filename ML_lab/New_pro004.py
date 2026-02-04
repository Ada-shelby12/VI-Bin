
# coding: utf-8

# In[32]:



#  SCATTTER PLOT
# Core scientific stack
#import numpy as np              # numerical computing
#import pandas as pd             # data manipulation
 
# plotting
#import seaborn as sns           # statistical visualization

# Machine learning (only if needed)
#import sklearn                  # scikit-learn (ML algorithms)
#import tensorflow as tf         # deep learning (optional)

import matplotlib.pyplot as plt

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
steps_walked=[8934,14902,3409,25672,12300,2023,6890]
plt.scatter(days,steps_walked,c="green")
plt.title('STEP COUNT',fontsize=20)
plt.ylabel('STEPS WALKED')
plt.xlabel('DAYS')
#to show the 
plt.show()


# In[30]:


# BAR GRAPH
plt.bar(days,steps_walked,color='blue',width=0.4)
plt.xlabel('Days')
plt.ylabel('Steps Count')
plt.show()


# In[22]:


# Line Plot
plt.plot(days,steps_walked)   #plot the Chart
plt.xlabel('Days OF the Week')
plt.ylabel('steps Walked')
plt.show()


# In[29]:


# PIE-Chart 

import pandas as pd 

data= {'Days':["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
'steps_walked':[8934,14902,3409,25672,12300,2023,6890]}

df = pd.DataFrame(data)

# Plot the Pie chart

plt.pie(df['steps_walked'], labels=df['Days'])
plt.title('Steps_Count')

plt.show()


# In[28]:


import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'days': ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    'steps_walked': [8934, 14902, 3409, 25672, 12300, 2023, 6890]
}

df = pd.DataFrame(data)

# Plot the Pie chart
plt.pie(
    df['steps_walked'],
    labels=df['days'],
    autopct='%1.1f%%',   # show percentages
    startangle=90        # rotate for better look
)
plt.title('Steps Count')
plt.show()

