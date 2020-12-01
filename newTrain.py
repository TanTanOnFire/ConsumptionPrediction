#this file should be run monthy or less
#more details are in Data.py

from sklearn.neural_network import MLPRegressor
from Data import ReadingData
from ConnectDB import Connection
import pickle
from joblib import dump, load

#this is train for 24 hours
def train(input_count,output_count):
    readingData=ReadingData()
    nh=readingData.getNH()
    clfs=[]
    fileName='MLP'
    for i in range(0,24):
        if i<10:
            hour='0'+str(i)
        else:
            hour=str(i)
        clfs.append(MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(nh,), random_state=1, activation='relu').
                    fit(readingData.getX(input_count,output_count,hour),readingData.getY(input_count,output_count,hour)))
        dump(clfs[i],fileName+str(i)+'.joblib')


#this is train for next 15 days

def trainMonth(input_count,output_count):
    readData=ReadingData()
    nh=readData.getNH(input_count,output_count)

    listx = readData.getXH1(input_count, output_count)
    #listPR = readData.getXH1(input_count, output_count)
    listy = readData.getYH1(input_count, output_count)
    print(listx)
    print(listy)
    #print(listPR)
    #nh = 7
    clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(nh,), random_state=1, activation='relu')
    clf.fit(listx, listy)
    dump(clf,'MLPDaily.joblib')
    #print(clf.predict(listPR))

#Uncomment this if you need them but before that update the csv file!
#train(5,7)
#trainMonth(15,5)
