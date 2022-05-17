#SPAM DETECTOR
from sklearn import datasets
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt


data=pd.read_csv(r"C:\Users\ADMIN\spam.csv",encoding=('ISO-8859-1'))
#print(data.info())
print(data.columns)
#print(data.head())
#labels=list()
#Converting 'ham'/'spam' into 0 and 1
    #method 1
'''k=0
for c in data['v1']:
    if c=='ham':
        labels.append(0)
        k=k+1
    else:
        labels.append(1)
        k=k+1'''
#print(labels)
#print(data.head())
    #method 2 
    #This method changes it for the original  data itself
data['v1']=data['v1'].map({'ham':0, 'spam':1})
#print(data.head())
#print(data.shape)

#Drop the empty value columns:
data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
#print(data.head())

data.drop_duplicates(inplace=True)
#print(data.isnull().sum()) #Missing data


# CountVectorizer is used to transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text.
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
x=data['v2']
y=data['v1']
x=cv.fit_transform(x)


from sklearn.model_selection import train_test_split
x_train_set,x_test_set,y_train_set,y_test_set=train_test_split(x,y, test_size=0.2, random_state=42)
print("Rows in Train set: ",x_train_set.shape, "Rows in test set: ",x_test_set.shape)
#print(train_set)


#from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
#model=KNeighborsClassifier()
model=MultinomialNB()
model.fit(x_train_set,y_train_set)
print(model.score(x_test_set,y_test_set))

# Prediction via the model
msg=input("ENTER THE MESSAGE: ")
vect=cv.transform([msg]).toarray()
predict=model.predict(vect)
if predict==[0]:
    print("\nITS A HAM!")
else:
    print("\nITS A SPAM!")

'''
# LOAD DUMP
import pickle
pickle.dump(model, open("spam.pkl","wb"))
pickle.dump(cv, open("vectorizer.pkl","wb"))

import streamlit as st
clf=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl,"rb"))

def main():
    st.title("EMAIL SPAM CLASSIFICATION: )

main()

'''


