import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


#load data
df = pd.read_csv("./data/heart_attack/Medicaldataset.csv")
# process column names
df.columns = [col.replace(" ","_").strip().lower() for col in df.columns]
# target featue : catgorical to numerical
df["result"] = df["result"].map({'negative':0, 'positive':1})

# seperate dependent and independent features
x = df.drop(columns="result")

y = df["result"]

# normalizatio for dependent features
x = np.log(x+1)
# split dependent data into train and test
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.2,random_state=42)
# scaling 
sc = StandardScaler()
sc.fit(x_train)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)
# save scaler for further use
pickle.dump(sc,open("../heart_attack_prediction/pickle_models/scaler.pkl","wb"))
# initialize model and fit training data
model =  RandomForestClassifier(  
                                criterion = 'gini',
                                max_depth = None,
                                max_features = 'sqrt',
                                min_samples_leaf = 1,
                                min_samples_split = 5,
                                n_estimators = 100
)

model.fit(x_train,y_train)
# save model for  further use
pickle.dump(model,open("../heart_attack_prediction/pickle_models/model.pkl","wb"))

print(f'Train score : {model.score(x_train,y_train)}')
print(f'Test score : {model.score(x_test,y_test)}')
