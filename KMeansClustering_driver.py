#Project 1 Step 4
#Gaby Ackermann Logan 
#IMPORT STATEMENTS
import KMeansClustering_functions as kmc 

#MAIN SCRIPT
glucose, hemoglobin, classification = kmc.openckdfile()
glucose_scaled, hemoglobin_scaled, classification = kmc.normalize(glucose, hemoglobin, classification)
newcentroids = kmc.generate_centroids(2)
print(newcentroids)

final_assignments,updated_centroids = kmc.clustering(newcentroids, hemoglobin_scaled, glucose_scaled)
print(final_assignments)
print(updated_centroids)

kmc.graphingkMeans(glucose_scaled, hemoglobin_scaled, final_assignments, updated_centroids)
kmc.accuracycalc(hemoglobin_scaled, glucose_scaled, classification, final_assignments)
