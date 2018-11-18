## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")
unique_regions = cars["origin"].unique()
print(unique_regions)

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)
dummy_years = pd.get_dummies(cars["year"],prefix = "year")
cars = pd.concat([cars,dummy_years],axis = 1)
cars = cars.drop(["cylinders","year"],axis=1)
cars.head()

## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]
split = int(.7*len(shuffled_cars))
train = shuffled_cars[0:split]
test = shuffled_cars[split:]
train.head()

## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression
models = {}
unique_origins = cars["origin"].unique()
unique_origins.sort()
cols = []
for col in train:
    if col.startswith(("cyl","year")) == True:
       cols.append(col) 
for o in unique_origins:
    lr = LogisticRegression()
    lr.fit(train[cols],train["origin"] == o)
    models[o] = lr


## 5. Testing the models ##

testing_probs = pd.DataFrame(columns=unique_origins)
cols = []
for col in test:
    if col.startswith(("cyl","year")) == True:
       cols.append(col) 
for o in unique_origins:
    testing_probs[o]= models[o].predict_proba(test[cols])[:,1]

## 6. Choose the origin ##

predicted_origins = testing_probs.idxmax(axis=1)
print(predicted_origins)