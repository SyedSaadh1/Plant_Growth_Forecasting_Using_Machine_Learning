from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
from sklearn import *
import numpy as np
import pandas as pd
from sklearn import *
from sklearn.metrics import accuracy_score
df = pd.read_csv('sugarcaneset.csv')
df["auxin"] = df["auxin"].map({'AuxinNA':1,'AuxinLow':2,'AuxinAN':3})
df["gibberellin"] = df["gibberellin"].map({'gibberellinNA':1,'gibberellinLow':2,'gibberellinAN':3})
df["cytokinin"] = df["cytokinin"].map({'cytokininNA':1,'cytokininLow':2,'cytokininAN':3})
df["ethylene"] = df["ethylene"].map({'ethyleneNA':1,'ethyleneLow':2,'ethyleneAN':3})
df["abscisicAcid"] = df["abscisicAcid"].map({'abscisicAcidNA':1,'abscisicAcidLow':2,'abscisicAcidAN':3})
df["nitrogen"] = df["nitrogen"].map({'NitrogenLow':1,'NitrogenAN':2,'NitrogenMN':3})
df["phosphorus"] = df["phosphorus"].map({'phosphorusLow':1,'phosphorusAN':2,'phosphorusMN':3})
df["magnesium"] = df["magnesium"].map({'magnesiumLow':1,'magnesiumAN':2,'magnesiumMN':3})
df["sulfur"] = df["sulfur"].map({'sulfurLow':1,'sulfurAN':2,'sulfurMN':3})
df["silicon"] = df["silicon"].map({'siliconLow':1,'siliconAN':2,'siliconMN':3})
df["plantGrowth"] = df["plantGrowth"].map({'HighGrowth':2,'MediumGrowth':1,'LowGrowth':0})
data = df[["auxin","gibberellin","cytokinin","ethylene","abscisicAcid","nitrogen","phosphorus","magnesium","sulfur","silicon","plantGrowth"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:1000]
training_outputs = outputs[:1000]
testing_inputs = inputs[1000:]
testing_outputs = outputs[1000:]
classifier = KNeighborsClassifier()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
print ("The accuracy of KNN Classifier on testing data is: " + str(accuracy))
testSet = [[1,1,2,3,1,1,2,1,1,3]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('KNN prediction on the first test set is:',predictions)
testSet = [[2,1,2,2,2,2,1,2,3,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('KNN prediction on the second test set is:',predictions)
testSet = [[3,2,1,3,3,2,1,3,2,3]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('KNN prediction on the third test set is:',predictions)
