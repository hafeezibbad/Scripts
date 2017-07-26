#!/usr/bin/python

"""
Building confusion matrix
"""

TP = 0     # Positive classified as positive
FN = 0      # Positive classified as negative


TN = 0    # Negative classified as negative
FP = 0     # Negative classified as positive

total = TP+FN+TN+FP
total_positive = TP + FN
total_negative = TN + FP

total_classified_positive = TP + FP
total_classified_negative = TN + FN

accuracy = (TP+TN)/(TP+TN+FP+FN)
print('Overall accuracy: {0}%'.format(accuracy*100))

positive_accuracy = TP/(TP+FN)
print('Accuracy for classifying positive: {0}%'.format(positive_accuracy*100))

negative_accuracy = TN/(TN+FP)
print('Accuracy for classifying negative: {0}%'.format(negative_accuracy*100))

precision=TP / (TP + FP)
print('Precision: {0}'.format(precision))

sensitivity = TP / (TP + FN)
print("Sensitivity:{0}%".format(sensitivity*100))
      
specificity = TN / (FP + TN)
print("Specificity: {0}%".format(specificity*100))

f_score = 2*TP /(2*TP + FP + FN)
print("F-Score: {0}".format(f_score))
