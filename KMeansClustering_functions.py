
#Project 1 Step 4
#Name: Gaby Ackermann Logan 

#Import Statements
import numpy as np
import matplotlib.pyplot as plt
import random

#Functions
def openckdfile():
#this function opens the ckd. txt file and separates classification, glucose, hemoglobin values
#into separate lists. This function takes no parameters and returns the new lists
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalize(glucose, hemolobin, classification):
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

def select(K):
    return np.random.random((K,2))

def generate_centroids(k):
#This function takes the parameter, k, and assignes a random number to glucose 
#hemoglobin for each centroid, keeping in the 0-1 range. It then returns the new
# scaled centroids
    centroids_generated = []
    for i in range (k):
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
#This function assigns and updates the centroids locatins and returns the final 
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
        assignK = final_assignments.sort()
        for i in range (K):
            updated_centroids[i][1]= np.mean(glucose_scaled[assignK==i])
            updated_centroids[i][0]= np.mean(hemoglobin_scaled[assignK==i])
        interations +=1
    return final_assignments, updated_centroids

def graphingkMeans(glucose_scaled, hemoglobin_scaled, final_assignments,newcentroids):
#This fucntion graphs the centroids and the clusters. It has no returns and takes the 
#scaled hemoglobin, glucose and centroids as parameters
    plt.figure()
    for i in range(len(updated_centroids)):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[final_assignments==i],glucose[final_assignments==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(newcentroids[i, 0], newcentroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

#Main Script
glucose, hemoglobin, classification = openckdfile()
glucose_scaled, hemoglobin_scaled, classification = normalize(glucose, hemoglobin, classification)
newcentroids = select(2)
final_assignments,updated_centroids = clustering(newcentroids,hemoglobin_scaled, glucose_scaled)
graphingkMeans(glucose_scaled, hemoglobin_scaled, final_assignments, updated_centroids)