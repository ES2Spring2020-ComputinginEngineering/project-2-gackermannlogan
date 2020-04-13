#Project 1,Steps 2 and 3
#Gaby Ackermann Logan 
#IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import random 

# FUNCTIONS
def openckdfile():
#This function opens the ckd.txt file and separates glucose, hemoglobin and classification 
#into separate lists and returns these list. Takes no parameters
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalize(glucose, hemoglobin, classification):
#This functions takes the parameters classification, glucose and hemoglobin lists
# and normailzes each value to fit into the range 0-1. It returns the new arrays of 
#glucose_scaled, and hemoglobin_scaled
    g = []
    h = []
    for l in glucose:
        newg = (l-70)/(490-70)
        g.append(newg)
    for l in hemoglobin:
        newh = (l- 3.1)/(17.8-3.1)
        h.append(newh)
    glucose_scaled = np.array(g)
    hemoglobin_scaled = np.array(h)
    classification = np.array(classification)
    return glucose_scaled, hemoglobin_scaled, classification

def GraphData(glucose, hemoglobin, classification):
#This function uses the original glucose, hemoglobin and classification values and graphs them.
#this function takes 3 paraemters and has no returns 
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification == 1], "b.", label = "Class = 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class = 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Hemoglobin v. Glucose")
    plt.legend()
    plt.show()
    
def Test_case():
#This Function creates random glucose and hemoglobin values and returns thes values 
#It takes no parameters
    newglucose = random.random()
    newhemoglobin = random.random()
    return newglucose, newhemoglobin

def calculateDistanceArray(newglucose,newhemoglobin, glucose_scaled, hemoglobin_scaled):
#This function calcualtes the distance between the randomly generated glucose and hemoglobin points 
#and returns the calculated distances. It takes 4 parameters, newglucose,newhemoglobin, glucose_scaled, hemoglobin_scaled
    newdistance = []
    for i in range(0,159):
        distance = np.sqrt(((newglucose-glucose_scaled)**2) +((newhemoglobin-hemoglobin_scaled)**2))
        newdistance.append(distance)
    distance_array = np.array(newdistance)
    return distance_array

def nearestneighborclassifier(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classificiation):
#This function takes determines the classification of the data points closest to the random test points generated
# and returns this calssification. It has 5 parameters, newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classificiation
    DistanceArray = calculateDistanceArray(newglucose,newhemoglobin, glucose_scaled, hemoglobin_scaled)
    min_index = np.argmin(DistanceArray)
    nearest_class = classification[min_index]
    return nearest_class

def GraphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification, nearest_class):
#This function plots the generated hemoglobin and glucose which make up the test case. 
# It has no returns and takes 5 parameters, newglucose, newhemoglobin, glucose, hemoglobin, classification
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    if nearest_class ==1:
        plt.plot(newglucose,newhemoglobin,"k.", markersize = 15, label= "CKD")
    else:
        plt.plot(newglucose, newhemoglobin, "r.", markersize = 15, label= "not CKD" )
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title ("Test Case")
    plt.legend()
    plt.show()
    
def knearestneighborclassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classificiation):
#This function finds the calssification of the "k" closest points to the test case and returns 
#the "k" classifcation. Takes 6 parameters, k, newglucose, newhemoglobin, glucose, hemoglobin, classificiation
    DistanceArray = calculateDistanceArray(newglucose,newhemoglobin, glucose_scaled, hemoglobin_scaled)
    sort_indicies = np.argsort(DistanceArray)
    kindicies = sort_indicies[:k]
    kclassification = classification[kindicies]
    return kclassification
 
# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
glucose_scaled, hemoglobin_scaled, classification = normalize(glucose, hemoglobin, classification)
newglucose, newhemoglobin = Test_case()

GraphData(glucose, hemoglobin, classification)
calculateDistanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled)
nearest_class = nearestneighborclassifier(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled,classification)
GraphTestCase(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification, nearest_class)
knearestneighborclassifier(3,newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled,classification)


