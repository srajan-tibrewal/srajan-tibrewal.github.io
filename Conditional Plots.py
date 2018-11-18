
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


titanic = pd.read_csv("train.csv")
titanic = titanic[["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]
titanic = titanic.dropna()                   


# In[5]:


titanic.head()


# In[6]:


import seaborn as sns 
import matplotlib.pyplot as plt


# In[9]:


sns.set_style("darkgrid")
sns.distplot(titanic["Age"])
plt.show()


# In[10]:


sns.kdeplot(titanic["Age"],shade = True)
plt.xlabel("Age")


# In[11]:


sns.set_style("white")
sns.kdeplot(titanic["Age"],shade = True)
plt.xlabel("Age")
sns.despine(left = True, bottom = True)


# In[13]:


g = sns.FacetGrid(titanic, col = "Pclass",size=6)
g.map(sns.kdeplot, "Age", shade = True)
sns.despine(left = True,bottom = True)
plt.show()


# In[14]:


g = sns.FacetGrid(titanic, col="Survived", row="Pclass")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()


# In[17]:


g = sns.FacetGrid(titanic, col="Survived", row="Pclass",hue='Sex',size = 3)
g.map(sns.kdeplot, "Age", shade=True)
g.add_legend()
sns.despine(left=True, bottom=True)

plt.show()

