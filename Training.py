import csv
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("finalised_dataset.csv",encoding='latin1')

X = data.drop('Soil_Name' ,axis=1)
X = X.drop('Crop' ,axis=1)
X1 = data['Soil_Name']
le.fit(X1)
labels = le.transform(data.Soil_Name)
X['crop'] = pd.Series(labels, index=X.index)

y = data['Crop']

encoder = LabelEncoder()
y = encoder.fit_transform(y)

model=RandomForestClassifier(n_estimators=100)
model.fit(X,y)
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
