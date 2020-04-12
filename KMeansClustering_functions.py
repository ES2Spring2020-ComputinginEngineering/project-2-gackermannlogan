#Please place your FUNCTION code for step 4 here.
#Import Statements
import numpy as np
import matplotlib.pyplot as plt
import random

#Functions
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def generate_centroids(k):
    centroids_scaled = []
    for i in range (k):
        g = random.uniform (0.0, 1.0)
        h = random.uniform(0.0, 1.0)
        centroids_scaled.append([g,h,i])
    newcentroids = np.array(centroids_scaled)
    return newcentroids

def calculateDistanceArray(newcentroids, glucose_scaled, hemoglobin_scaled):
    distance_array = []
    for i in range(0,159):
        distance_array = np.sqrt(((newcentroids[0]-glucose_scaled)**2) +((newcentroids[1]-hemoglobin_scaled)**2))
    return distance_array

def clustering(k, hemoglobin_scaled, glucose_scaled):
    assigments = []
    newcentroids = generate_centroids(k)
    distances = np.zeros((k, len(hemoglobin_scaled)))
    for i in range(k):
        g = newcentroids[i,1]
        h = newcentroids[i,0]
        distances[i] = calculateDistanceArray(newcentroids, g, h)
       
    assignments = np.argmin(distances, axis = 0)  
    assigments.append(newcentroids, glucose_scaled, hemoglobin_scaled)
    newassignment = np.array(assignments)
    classifications = newassignment[:,2]
    print(classifications)
    return classifications


#Main Script
glucose, hemoglobin, classification = openckdfile()
hemoglobin_scaled = (hemoglobin- 3.1)/(17.8-3.1)
glucose_scaled = (glucose-70)/(490-70)
k = 10
newcentroids, classifications = clustering(k, glucose_scaled, hemoglobin_scaled)
plt.figure()
plt.plot(hemoglobin_scaled[classifications==1],glucose_scaled[classifications==1], "k.", label = "Class 1")
plt.plot(hemoglobin_scaled[classifications==0],glucose_scaled[classifications==0], "r.", label = "Class 0")
plt.xlabel("Scaled Hemoglobin")
plt.ylabel("Scaled Glucose")
plt.legend()
plt.show()


