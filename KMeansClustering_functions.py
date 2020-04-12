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
    for i in glucose:
        newg = (i-70)/(490-70)
        g.append(newg)
    for i in hemoglobin:
        newh = (i- 3.1)/(17.8-3.1)
        h.append(newh)
    hemoglobin_scaled = np.array(h)
    glucose_scaled = np.array(g)
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
        g = random.uniform (0.0, 1.0)
        h = random.uniform(0.0, 1.0)
        centroids_generated.append([g,h,i])
    newcentroids = np.array(centroids_generated)
    return newcentroids

def assign(newcentroids, hemoglobin_scaled, glucose_scaled):
    K = newcentroids.shape[0]
    distances = np.zeros((K, len(hemoglobin)))
    for i in range(K):
        new_glucose = glucose[i]
        new_hemoglobin = hemoglobin[i]
        distances= calculateDistanceArray(K, new_glucose, new_hemoglobin)
        assignments = np.argmin(distances, axis = 0)    
        c = assignments[2]
        assign.append([c,new_glucose,new_hemoglobin])
    final_assignment = np.array(assign)
    return final_assignment

def calculateDistanceArray(newcentroids, glucose, hemoglobin):
    d = []
    for i in range(0,159):
        distance= np.sqrt(((newcentroids[0]-glucose)**2) +((newcentroids[1]-hemoglobin)**2))
        d.append(distance)
    finaldistance = np.array(d)
    return finaldistance

def update(final_assignment, glucose_scaled, hemoglobin_scaled, newcentroids):
    K = newcentroids.shape[0]
    updated_centroids = np.zeros((K,2))
    assignK = final_assignment.sort()
    for i in range (0, 159):
        update_glucose = np.mean(glucose[assignK==i])
        update_hemoglobin = np.mean(hemoglobin[assignK ==i])
        updated_centroids[i] = np.append(update_glucose, update_hemoglobin)
    return updated_centroids

def graphingkMeans(glucose, hemoglobin, assignment,centroids):
    plt.figure()
    for i in range(assignment.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 0], centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

#Main Script
glucose, hemoglobin, classification = openckdfile()
glucose_scaled, hemoglobin_scaled, classification = normalize(glucose, hemoglobin, classification)
newcentroids = select(5)
final_assignment = assign(newcentroids, hemoglobin_scaled, glucose_scaled)
updated_centroids = update(final_assignment, glucose, hemoglobin, newcentroids)
graphingkMeans(glucose_scaled, hemoglobin_scaled, final_assignment, updated_centroids)