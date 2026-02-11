
# coding: utf-8

# In[1]:


from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score

# Actual Labels
# 1 = Positive, 0 = Negative
y_true = [1]*11 + [0]*9

# Predicted Labels
y_pred = [1]*8 + [0]*3 + [1]*4 + [0]*5

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:")
print(cm)

# Evaluation Metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("\nEvaluation Metrics:")
print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall :", recall)
print("F1-Score :", f1)

# Detailed classification report
print("\nClassification Report: ")
print(classification_report(y_true, y_pred))


# In[2]:


from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score

# Define counts
TP = 950
TN = 700
FN = 200
FP = 150

# Construct actual labels
# 1 = Positive, 0 = Negative
y_true = [1]* (TP + FN) + [0]* (TN + FP)

# Construct predicted labels
y_pred = [1]*TP + [0]*FN + [1]*FP + [0]*TN

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:")
print(cm)

# Evaluation Metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("\nEvaluation Metrics:")
print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall :", recall)
print("F1-Score :", f1)

# Detailed classification report
print("\nClassification Report: ")
print(classification_report(y_true, y_pred))


# In[4]:


from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score

# Define counts
TP = 950
TN = 150
FN = 200
FP = 700
# Construct actual labels
# 1 = Positive, 0 = Negative
y_true = [1]* (TP + FN) + [0]* (TN + FP)

# Construct predicted labels
y_pred = [1]*TP + [0]*FN + [1]*FP + [0]*TN

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:")
print(cm)

# Evaluation Metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("\nEvaluation Metrics:")
print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall :", recall)
print("F1-Score :", f1)

# Detailed classification report
print("\nClassification Report: ")
print(classification_report(y_true, y_pred))

