# #import Excell
# import pandas as pd
# covid_data = pd.read_excel("covid_classification_data.xlsx")

# #put data from columns to variables
# Actual_data = covid_data['Actual'].tolist()
# Predict_data = covid_data["Predicted"].tolist()
# print ("Actual_Data: ",Actual_data)
# print ("Predict_Data: ",Predict_data)

# #Recall sk-learn libraries for using metrics
# from sklearn.metrics import accuracy_score
# Acurracy = accuracy_score(Actual_data,Predict_data)
# from sklearn.metrics import precision_score
# Precision = precision_score(Actual_data,Predict_data)
# from sklearn.metrics import recall_score
# Recall = recall_score(Actual_data,Predict_data)
# from sklearn.metrics import f1_score
# score = f1_score(Actual_data,Predict_data)
# from sklearn.metrics import confusion_matrix
# Confusion = confusion_matrix(Actual_data, Predict_data)


# #print final results
# print ("Accuracy is: ", Acurracy*100)
# print ("Precision is: ",Precision*100)
# print ("Recall is: ", Recall*100)
# print ("F1-score is: ", score*100)
# print("Confusion Matrix:\n ", Confusion)


# #plot 
# from matplotlib import pyplot as plt
# plt.plot(Actual_data,Predict_data,color="red")
# plt.show()

import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def load_data(file_path):
    """Load Excel data."""
    return pd.read_excel(file_path)

def calculate_metrics(actual, predicted):
    """Calculate evaluation metrics."""
    return {
        "Accuracy": accuracy_score(actual, predicted),
        "Precision": precision_score(actual, predicted),
        "Recall": recall_score(actual, predicted),
        "F1 Score": f1_score(actual, predicted)
    }

# Load data
covid_data = load_data("covid_classification_data.xlsx")

# Extract actual and predicted values
actual_data = covid_data['Actual'].tolist()
predicted_data = covid_data['Predicted'].tolist()

# Calculate metrics
metrics = calculate_metrics(actual_data, predicted_data)

# Print results
for metric, value in metrics.items():
    print(f"{metric} is: {value * 100:.2f}%")
