#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset('titanic')
sns.countplot(x='class', data=titanic)
plt.title('Number of passengers by class')
plt.show()
sns.histplot(data=titanic, x='age', kde=False)
plt.title('Age of passengers')
plt.show()


# In[ ]:




