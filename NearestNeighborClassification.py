#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt
import random


# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification
def Test_case():
    newglucose = np.random.random(1)
    newhemoglobin = np.random.random(1)
    return newglucose, newhemoglobin

def calculateDistanceArray(newglucose,newhemoglobin, glucose, hemoglobin):
    distance_array = []
    for i in range(0,159):
        distance_array = np.sqrt(((newglucose-glucose)**2) +((newhemoglobin-hemoglobin)**2))
    return distance_array

def nearestneighborclassifier(newglucose, newhemoglobin, glucose, hemoglobin, classificiation):
    min_index_hemoglobin = np.argmin(distancearray[0])
    nearest_class_hemoglobin = classification[min_index_hemoglobin]
    min_index_glucose = np.argmin(distancearray[1])
    nearest_class_glucose = classification[min_index_glucose]
    return nearest_class_hemoglobin, nearest_class_glucose

def knearestneighborclassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classificiation):
    sorted_indices_hemoglobin = np.argsort(distancearray[0])
    k_indices_hemoglobin = sorted_indices_hemoglobin[:k]
    k_classification_hemoglobin = classification[k_indices_hemoglobin]
    sorted_indices_glucose = np.argsort(distancearray[1])
    k_indices_glucose = sorted_indices_glucose[:k]
    k_classification_glucose = classification[k_indices_glucose]
    return k_classification_hemoglobin,k_classification_glucose

# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
hemoglobin_scaled = (hemoglobin- 3.1)/(17.8-3.1)
glucose_scaled = (glucose-70)/(490-70)
Testcase = Test_case()
distancearray = calculateDistanceArray(Testcase,Testcase, glucose_scaled, hemoglobin_scaled)
newneighbor = nearestneighborclassifier(Testcase, Testcase, glucose_scaled, hemoglobin_scaled,classification)
kneighbor = knearestneighborclassifier(3,Testcase, Testcase, glucose_scaled, hemoglobin_scaled,classification)
plt.figure()
plt.figure()
plt.plot(Testcase[classification==newneighbor], Testcase[classification == newneighbor], "b.", label = "Test Case 1",markersize =12)
plt.plot(hemoglobin_scaled[classification==1],glucose_scaled[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin_scaled[classification==0],glucose_scaled[classification==0], "r.", label = "Class 0")
plt.xlabel("Hemoglobin Scaled")
plt.ylabel("Glucose Scaled")
plt.legend()
plt.show()
