import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('C:\\Users\\Kanishk Wadhwa\\MLAPP\\trainloan.csv')
for column in ['Gender','Married','Dependents','Self_Employed','Loan_Amount_Term','Credit_History']:
    df[column].fillna(df[column].mode()[0],inplace=True)

df['LoanAmount']=df['LoanAmount'].fillna(df['LoanAmount'].dropna().mean())
df['Dependents'] = df['Dependents'].str.rstrip('+')
df['Gender'] = df['Gender'].map({'Female':0,'Male':1}).astype(np.int)
df['Married'] = df['Married'].map({'No':0, 'Yes':1}).astype(np.int)
df['Education'] = df['Education'].map({'Not Graduate':0, 'Graduate':1}).astype(np.int)
df['Self_Employed'] = df['Self_Employed'].map({'No':0, 'Yes':1}).astype(np.int)
df['Loan_Status'] = df['Loan_Status'].map({'N':0, 'Y':1}).astype(np.int)
df['Dependents'] = df['Dependents'].astype(np.int)

array =df.values

X=array[:,6:10]
X=X.astype('int')
y=array[:,12]
y=y.astype('int')
#X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

lr=LogisticRegression()
lr.fit(X,y)

pickle.dump(lr, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))