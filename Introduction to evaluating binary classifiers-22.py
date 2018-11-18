## 1. Introduction to the Data ##

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv("admissions.csv")
model = LogisticRegression()
model.fit(admissions[["gpa"]], admissions["admit"])
labels = model.predict(admissions[["gpa"]])
admissions["predicted_label"] = labels
print(admissions["predicted_label"].value_counts())
print(admissions.head())

## 2. Accuracy ##

admissions.rename(columns={'admit': 'actual_label'}, inplace=True)
matches = (admissions["predicted_label"] == admissions["actual_label"])
correct_predictions = admissions[admissions["actual_label"] == admissions["predicted_label"]]
print(correct_predictions.head())
accuracy = len(correct_predictions)/len(admissions["actual_label"])

## 4. Binary classification outcomes ##

t_p = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[t_p])
true_negatives = len(admissions[(admissions["predicted_label"] == 0) & (admissions["actual_label"] == 0)])
print(true_negatives)
print(true_positives)

## 5. Sensitivity ##

# From the previous screen
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])
false_negatives = len(admissions[(admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)])
sensitivity = true_positives / (true_positives+false_negatives)

## 6. Specificity ##

# From previous screens
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])
false_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)
false_negatives = len(admissions[false_negative_filter])
true_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 0)
true_negatives = len(admissions[true_negative_filter])
false_positives = len(admissions[(admissions["predicted_label"] == 1) & (admissions["actual_label"] == 0)]) 
specificity = true_negatives/(true_negatives+false_positives)