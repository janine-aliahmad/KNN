# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:26:52 2023

@author: Janin
"""
import csv
import random

def store_data():
    """stores data in a list called data_set"""
    data_set=[] #[[param1,param2,param3,param4,param5,param6,classe],[...]...]
    with open(r"D:\Janine's Documents\ESILV\S5\DATA IA\dataset (1).csv", 'r') as data:
        reader=csv.reader(data,delimiter=';')
        for row in reader:
            L=[]
            for col in range(6): #we add all 6 parameters
                value=float(row[col])
                L.append(value)
            classe=float(row[6]) #we add the class
            L.append(classe)
            data_set.append(L)
    data.close()
    return data_set

def prediction_KNN(data_set,data,k):
    """predicts the class of the given data using data_set as reference"""
    distances=[] #[[distance,poids,classe correspondante]],[...],...]
    
    #calculate distances with every data in our data_set and store them
    for i in range(len(data_set)):
        l=[] #[distance, poids, classe correspondante]
    
        #distance euclidienne:
        #d=(data[0]-data_set[i][0])**2+(data[1]-data_set[i][1])**2+(data[2]-data_set[i][2])**2+(data[3]-data_set[i][3])**2+(data[4]-data_set[i][4])**2+(data[5]-data_set[i][5])**2
        
        #distance chebybchev:
        #d=max(abs(data[0]-data_set[i][0]),abs(data[1]-data_set[i][1]),abs(data[2]-data_set[i][2]),abs(data[3]-data_set[i][3]),abs(data[4]-data_set[i][4]),(data[5]-data_set[i][5]))
            
        #distance manhattan:
        d=abs(data[0]-data_set[i][0])+abs(data[1]-data_set[i][1])+abs(data[2]-data_set[i][2])+abs(data[3]-data_set[i][3])+abs(data[4]-data_set[i][4])+(data[5]-data_set[i][5])
        poids=1/(d+1) #we add +1 to avoid issues with d=0
        
        l.append(d)
        l.append(poids)
        l.append(data_set[i][6]) #we add the class
        distances.append(l)
   
    #sort according to distance
    distances.sort(key=lambda x:x[0])
    
    #calculation of class with the most weight (poids) among the k shortest distances
    nb_1=0
    nb_0=0
    for i in range(k): # we calculate weight results for the k shortest distances
        if distances[i][2]==1:
            nb_1=nb_1+distances[i][1] #we sum the weights
        elif distances[i][2]==0:
            nb_0=nb_0+distances[i][1] #we sum the weights
    class_pred=0 if max(nb_0,nb_1)==nb_0 else 1 #we choose class with highest weight
    
    return class_pred
        
def KNN(data , k):
    """predicts classe of data using KNN algo"""
    
    data_set=store_data()
    random.shuffle(data_set) #allows randomization to avoid local best solution
    class_pred=prediction_KNN(data_set, data, k)
    
    return class_pred
   
def preTest():
    """allows us to run tests on the test data set to find the best k for the given data set, returns accuracy based on k"""
    
    #store pretest data
    pretest_set=[] #[[param1,param2,param3,param4,param5,param6,classe],[...]...]
    with open(r"D:\Janine's Documents\ESILV\S5\DATA IA\pretest.csv", 'r') as data:
        reader=csv.reader(data,delimiter=';')
        for row in reader:
            L=[]
            for col in range(6):
                value=float(row[col])
                L.append(value)
            classe=float(row[6])
            L.append(classe)
            pretest_set.append(L)
    data.close()
    
    #predict class for every data in set, compare with real class
    best_k=1
    max_accuracy=0
    for k in range(1,26): #test best k between 1 and 25 
        accuracy=0
        correct=0
        for test in pretest_set: #prediction for ever data in test set
            class_pred=KNN(test,k)
            if class_pred==test[6]: #count how many correct predictions
                correct=correct+1
        accuracy=correct/len(pretest_set) #calculate accuracy for every k 
        print("for k=",k," accuracy= ",accuracy)
        
        #store best k to return it 
        if max(max_accuracy,accuracy)==accuracy:
            max_accuracy=accuracy
            best_k=k
    
    return best_k

#pretest takes a long time but we conclude that best combination for highest accuracy is manhattan with k=4

def finalTest():
    """generates predicted class for every data item in given Final data set and stores result in a txt file"""
    
    #store final data
    finaltest_set=[] #[[param1,param2,param3,param4,param5,param6],[...]...]
    with open(r"D:\Janine's Documents\ESILV\S5\DATA IA\finaltest.csv", 'r') as data:
        reader=csv.reader(data,delimiter=';')
        for row in reader:
            L=[]
            for col in range(6):
                value=float(row[col])
                L.append(value)
            finaltest_set.append(L)
    data.close()
    
    #write class predictions for data in a file
    with open(r"D:\Janine's Documents\ESILV\S5\DATA IA\ALI AHMAD JANINE_ALIYEVA ROYA_GROUPE A.txt",'w') as result:
        for test in finaltest_set:
            class_pred=KNN(test,4) #we predict class for ever data
            result.write(str(class_pred)+"\n") #we write prediction in file
    result.close()
    
    return "Done"
        