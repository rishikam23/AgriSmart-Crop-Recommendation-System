import pandas as pd
from sklearn.naive_bayes import GaussianNB
import pickle
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv("Crop_recommendation.csv")
features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)

from sklearn.naive_bayes import GaussianNB
NaiveBayes = GaussianNB()
NaiveBayes.fit(Xtrain,Ytrain)

pickle.dump(NaiveBayes,open('NaiveBayes.pkl','wb'))
NaiveBayes=pickle.load(open('NaiveBayes.pkl','rb'))