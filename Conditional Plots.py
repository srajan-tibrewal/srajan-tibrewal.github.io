#Code for implementing conditional plots
# dataset encoding: utf-8

import pandas as pd


# import dataset and choose columns, display dataframe
titanic = pd.read_csv("train.csv")
titanic = titanic[["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]
titanic = titanic.dropna()                   
titanic.head()


# Import plotting libraries


import seaborn as sns 
import matplotlib.pyplot as plt


# Code for different kinds of conditional plots made. Best viewed in jupyter notebook


sns.set_style("darkgrid")
sns.distplot(titanic["Age"])
plt.show()

sns.kdeplot(titanic["Age"],shade = True)
plt.xlabel("Age")


sns.set_style("white")
sns.kdeplot(titanic["Age"],shade = True)
plt.xlabel("Age")
sns.despine(left = True, bottom = True)

g = sns.FacetGrid(titanic, col = "Pclass",size=6)
g.map(sns.kdeplot, "Age", shade = True)
sns.despine(left = True,bottom = True)
plt.show()

g = sns.FacetGrid(titanic, col="Survived", row="Pclass")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

g = sns.FacetGrid(titanic, col="Survived", row="Pclass",hue='Sex',size = 3)
g.map(sns.kdeplot, "Age", shade=True)
g.add_legend()
sns.despine(left=True, bottom=True)

plt.show()

