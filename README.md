Gaby Ackermann Logan 
ES2 - Project 2: Biomedical Data Analysis

DESCRIPTION: This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org). In this project, three algorithms are implemented: Nearest Neighbor, K-Nearest Neighbor and K-means Cluster. The goal was to generate a random test case and classify the data as either CKD or not CKD correctly based on these algorithms. 

INSTRUCTIONS:There are 3 documents contained in this project - the "NearestNeighborClassification.py," "KMeansCLustering_functions.py" and "KMeansClustering_driver.py" The descriptions of the file and the functions contained are below. 

1) The NearestNeighborClassification.py- This includes both the Nearest Neighbor Classification and K-Nearest Neighbor Classification methods. The Nearest Neighbor classifies a random data point as either a part of the 0 or 1 class based on the "nearest" neighbor's classification. Hence the name. The K-Nearest Neighbor is similar but it takes multiple neighboring points to classify the new data point. 

FUNCTIONS:
Def openckdfile():
Arguments - Takes no parameters
Function - Uploads and opens the data file that will be used in the project 
Return - Returns the glucose, hemoglobin and classification values into separate lists

Def normalize():
Arguments - Takes the glucose, hemoglobin and classification lists as parameters
Function - Normalizes each of the glucose and hemoglobin values to fit on the 0-1 scale 
Return - Returns the new glucose_scaled, hemoglobin_scaled arrays and the classification which was unchanged 

Def GraphData():
Arguments - Takes the original glucose, hemoglobin and classification values as parameters
Function - Graphs the original glucose and hemoglobin values 
Returns - None

Def Test_case():
Arguments - Takes no parameters
Function - crease random glucose and hemoglobin values 
Return - Returns the newglucose and newhemoglobin random values 

Def calculateDIstanceArray():
Arguments - Takes the randomly chosen values for glucose and hemoglobin (newglucose and newhemoglobin) and the scaled glucose and hemoglobin values 
Function - Calculates the distance between the randomly generated glucose and hemoglobin values and the scaled glucose and hemoglobin values 
Return - Returns the calculated distance as an array (distance_array)

Def nearestneighborclassifier():
Arguments - Takes the randomly generated values for glucose and hemoglobin (newglucose and newhemoglobin) as well as the scaled glucose and hemoglobin values and the original classification list 
Function - Determines the classification of the data points closest to the random test points generated
Return - Returns the classification of the nearest points 

Def knearestneighborclassifier():
Arguments - Takes the number of points (k),the randomly generated values for glucose and hemoglobin (newglucose and newhemoglobin) as well as the scaled glucose and hemoglobin values and the original classification list 
Function - Determines the classification of the k closest points to the test case
Return - Returns the classification 

In the main script are the graphs for the original data and the nearest neighbor. To run the code, pick a value for k in the knearestneighborclassifier function (last one at the bottom of the script) and then click RUN.

2) The KMeansClustering_functions.py - This contains the functions required to run the KMeansClustiner_driver.py.

FUNCTIONS:
Def openckdfile():
Arguments - Takes no parameters
Function - Uploads and opens the data file that will be used in the project 
Return - Returns the glucose, hemoglobin and classification values into separate lists

Def normalize():
Arguments - Takes the glucose, hemoglobin and classification lists as parameters
Function - Normalizes each of the glucose and hemoglobin values to fit on the 0-1 scale 
Return - Returns the new glucose_scaled, hemoglobin_scaled arrays and the classification which was unchanged 

Def generate_cetroids():
Arguments - Takes the number of centroids, K, as a parameter 
Function - Assigns a random value to glucose and hemoglobin for each centroid, keeping in the 0-1 range 
Return - Returns the new scaled centroids (newcentroids) 

Def calculatedDistanceArray():
Arguments - Takes the randomly generated, scaled centroids (newcentroids) and the scaled glucose and hemoglobin as parameters
Function - Calculates the distance between the scaled hemoglobin and glucose points and generated centroid points
Return - Returns the calculated distance 

Def clustering():
Arguments - Takes the generated centroids (newcentroids) and the scaled hemoglobin and glucose values as parameters 
Function - Assigns and updates the centroids' location 
Return - Returns the new array of centroids(updated_centroids) and classifications(final_assignments)

Def graphingMeans():
Arguments - Takes the scaled hemoglobin and glucose values, the new classifications and the new centroid locations as parameters
Function - Graphs the centroids and clusters 
Return - Has no returns 

Def accuracycalc():
Arguments - Takes the scaled hemoglobin, glucose values, the original classification list and and new classifications as parameters
Function - Calculates the true positives, negatives and false positive negatives as a percentage and prints these percentages 
Return - Returns the calculated true positives, negatives and false positives and negatives

To run the code, go to the KMeanClustering_driver.py file 

3) The KMeansClustering_driver.py - This is the "main script" of the KMeanClustering_functions.py. To run the code, pick a value for k in select function and then click RUN. Make sure that before each function is a "kmc" as it calls the function definitions from the KMeanClustering_functions.py file.


 