
#Project 1 Step 4
#Name: Gaby Ackermann Logan 

#IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import random

#FUNCTIONS
def openckdfile():
#this function opens the ckd. txt file and separates classification, glucose, hemoglobin values
#into separate lists. This function takes no parameters and returns the new lists
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalize(glucose, hemoglobin, classification):
#this functions takes the parameters classification, glucose and hemoglobin lists
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

def generate_centroids(K):
#This function takes the parameter, k, and assignes a random number to glucose 
#hemoglobin for each centroid, keeping in the 0-1 range. It then returns the new
# scaled centroids
    centroids_generated = []
    for i in range (K):
        g = random.uniform (0,1)
        h = random.uniform(0,1)
        centroids_generated.append([g,h,i])
    newcentroids = np.array(centroids_generated)
    return newcentroids

def calculateDistanceArray(newcentroids, glucose_scaled, hemoglobin_scaled):
#This function calculates the distance between the scaled hemoglobin and glucose points
#and each centroid and then returns the calculatted distances. It takes the
#new array of centroids and the scaled hemolgobin and glucose as parameters
    newdistance = []
    for i in range(len(newcentroids)):
        centroid_array = newcentroids[i]
        distance = np.sqrt(((centroid_array[0]-glucose_scaled)**2) +((centroid_array[1]-hemoglobin_scaled)**2))
        newdistance.append(distance)
    distance_array = np.array(newdistance)
    return distance_array

def clustering(newcentroids,hemoglobin_scaled, glucose_scaled):
#This function assigns and updates the centroids' locatins and returns the final 
#locations and classifications 
#it takes the the new array of centroids and the scaled hemolgobin and glucose as parameters
    interations = 0
    while interations < 100:
        K = newcentroids.shape[0]
        distance = np.zeros((K, len(hemoglobin_scaled)))
        for i in range(K):
            distance = calculateDistanceArray (newcentroids, glucose_scaled, hemoglobin_scaled)
        final_assignments = np.argmin(distance, axis = 0)
        updated_centroids = np.zeros((K,2))
        assignK = final_assignments
        for i in range (K):        
            updated_centroids[i][1] = np.mean(glucose_scaled[assignK==i])        
            updated_centroids[i][0] = np.mean(hemoglobin_scaled[assignK==i])    
        print(updated_centroids)
        interations +=1
    return final_assignments, updated_centroids

def graphingkMeans(glucose_scaled, hemoglobin_scaled, final_assignments,updated_centroids):
#This fucntion graphs the centroids and the clusters. It has no returns and takes the 
#scaled hemoglobin, glucose and centroids as parameters
    plt.figure()
    for i in range(int(final_assignments.max()+1)):
        rcolor = np.random.rand(3)
        plt.plot(hemoglobin_scaled[final_assignments==i],glucose_scaled[final_assignments==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(updated_centroids[i,0], updated_centroids[i,1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("K Mean ")
    plt.legend()
    plt.show()
    
def accuracycalc(classification, final_assignments):
#This function calculates the true positives and negatives and false postives and negatives as a precentrage
# and prints the percentages of each. It takes 4 paramenters, hemoglobin_scaled, glucose_scaled, classification, final_assignments
    TruePos = 0
    FalsePos = 0
    TrueNeg = 0
    FalseNeg = 0
    Total = 0
    for i in range(len(classification)):
        if (final_assignments[i]==1 and classification[i]==1):
            TruePos += 1
            Total +=1
        if (final_assignments[i]==1 and classification[i]==0):
            FalsePos += 1
            Total +=1
        if (final_assignments[i]==0 and classification[i]==0):
            TrueNeg += 1
            Total +=1
        if (final_assignments[i]==0 and classification[i]==1):
            FalseNeg += 1
            Total +=1
    truePositives = (TruePos/Total)*100
    falsePositives = (FalsePos/Total)*100
    trueNegatives = (TrueNeg/Total)*100
    falseNegatives = (FalseNeg/Total)*100
    print("The True Positives rate is", truePositives, "%")
    print("The False Positives rate is", falsePositives, "%")
    print("The True Negatives rate  is", trueNegatives, "%")
    print("The False Negatives rate is", falseNegatives, "%")
    return TruePos, FalsePos, TrueNeg, FalseNeg
