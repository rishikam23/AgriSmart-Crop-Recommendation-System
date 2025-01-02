from __future__ import print_function
import pandas as pd
import warnings
import pickle
warnings.filterwarnings('ignore')
df = pd.read_csv("Crop_recommendation.csv")
features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)

from sklearn.ensemble import RandomForestClassifier

RF = RandomForestClassifier(n_estimators=20, random_state=0)
RF.fit(Xtrain,Ytrain)

pickle.dump(RF,open('rfmodel.pkl','wb'))
rfmodel=pickle.load(open('rfmodel.pkl','rb'))