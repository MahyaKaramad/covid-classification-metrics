#import Excell
import pandas as pd
covid_data = pd.read_excel("covid_classification_data.xlsx")

#put data from columns to variables
Actual_data = covid_data['Actual'].tolist()
Predict_data = covid_data["Predicted"].tolist()
print ("Actual_Data: ",Actual_data)
print ("Predict_Data: ",Predict_data)

#Recall sk-learn libraries for using metrics
from sklearn.metrics import accuracy_score
Acurracy = accuracy_score(Actual_data,Predict_data)
from sklearn.metrics import precision_score
Precision = precision_score(Actual_data,Predict_data)
from sklearn.metrics import recall_score
Recall = recall_score(Actual_data,Predict_data)
from sklearn.metrics import f1_score
score = f1_score(Actual_data,Predict_data)
from sklearn.metrics import confusion_matrix
Confusion = confusion_matrix(Actual_data, Predict_data)


#print final results
print ("Accuracy is: ", Acurracy*100)
print ("Precision is: ",Precision*100)
print ("Recall is: ", Recall*100)
print ("F1-score is: ", score*100)
print("Confusion Matrix:\n ", Confusion)

