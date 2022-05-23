import numpy as np
import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

filename = 'finalized_model.sav'



def get(T,WS,Pre,H,N,P,K,soil_type):
    
    data = pd.read_csv("finalised_dataset.csv",encoding='latin1')

    y = data['Crop']
    encoder = LabelEncoder()
    y = encoder.fit_transform(y)

    X1 = data['Soil_Name']
    le.fit(X1)

    C = le.transform(pd.Series(soil_type))[0]

    xx = [[T,WS,Pre,H,N,P,K,C]]

    loaded_model = pickle.load(open(filename, 'rb'))
    result_encoded = loaded_model.predict(xx)

    Show_Result = encoder.inverse_transform([result_encoded])[0]

    print(Show_Result)
    return Show_Result 

##k = get(M,H,T,soil_type)
##
##print("Show_Result : ",k)


    
