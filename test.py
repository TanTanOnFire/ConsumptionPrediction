#This is our final file actually this file should be run once a day and will insert
#the data per next 24 hour!
from ConnectDB import Connection
from joblib import dump, load
from datetime import datetime
class Test:
    lastDate=datetime
    def test(self,sensorID):
        clfss=[]
        energyInHour=[]
        time=[]
        obj1=Connection(200)
        rec=obj1.getTheLastRecord(220,5)
        for row in rec:
            time.append(str(row[3]))
            energyInHour.append(row[1])
        for i in range(0,24):
            condition = time[i].split(' ')
            tempDateMonth = int(time[i].split(' ')[0].split('-')[1])
            tempDateDay = int(time[i].split(' ')[0].split('-')[2])
            tempDateYear = int(time[i].split(' ')[0].split('-')[0])
            firstDate= datetime(int(time[i].split(' ')[0].split('-')[0]),int(time[i].split(' ')[0].split('-')[1]),int(time[i].split(' ')[0].split('-')[2]))
            if tempDateMonth > 6 and tempDateMonth != 12:
                if tempDateDay == 30:
                    tempDateDay = 1
                    tempDateMonth += 1
                else:
                    tempDateDay += 1

            elif tempDateMonth == 12:
                if tempDateDay == 29:
                    tempDateDay = 1
                    tempDateMonth = 1
                else:
                    tempDateYear += 1
            else:
                if tempDateDay == 31:
                    tempDateDay = 1
                    tempDateMonth += 1
                else:
                    tempDateDay += 1

            if condition.__len__() > 1:
                date=str(datetime(tempDateYear,
                         tempDateMonth,
                         tempDateDay,
                         int(time[i].split(' ')[1].split(':')[0]),
                         int(time[i].split(' ')[1].split(':')[1]),
                         int(time[i].split(' ')[1].split(':')[2])))
                timeI = time[i].split(' ')[1].split(':')[0]
                print(timeI)

                prd1 = []

                for j in range(0,time.__len__()):
                    if time[j].split(' ').__len__()>1:
                        if int(time[j].split(' ')[1].split(':')[0]) ==int(timeI):
                            print('this is index' + str(j))
                            print(energyInHour[j])
                            prd1.append(float(energyInHour[j]))
                print(prd1)



            else:
                if condition.__len__()<=1:
                    date = str(datetime(tempDateYear,
                                    tempDateMonth,
                                    tempDateDay,0,0,0))

                    print('hey')
                    timeI = time[i].split(' ')[0]
                    print(timeI)

                    prd1 = []

                    for j in range(0,time.__len__()):
                        condition2 = time[j].split(' ')

                        if condition2.__len__()==1:
                            print(condition2)
                            if  time[j].split(' ').__len__()== timeI.split(' ').__len__():
                                print('heeeey')
                                print('this is index' + str(j))
                                print(energyInHour[j])
                                prd1.append(float(energyInHour[j]))

            print(prd1.__len__())
            print(date)
            print(firstDate)
            clfss = load('MLP' + str(i)+ '.joblib')
            list=[]
            for i in range(0,5):
                list.append(prd1[i])
            predictedEnergy=float(clfss.predict([list]))
            obj1.connectToDatabaseHourly(predictedEnergy,sensorID,date)

    def getInputDataset(self,sensorID,counter1,counter2):
        predictedTimeReal = []
        predictList = []
        predictedTime = []
        obj2 = Connection(sensorID)
        record = obj2.getTheLastRecordMonthly(sensorID, counter1)
        record2 = obj2.getTheLastRecordMonthlyPredicted(sensorID, counter2)
        for row in record:
            predictList.append(float(row[1]))
            predictedTimeReal.append(str(row[3]))
        for row in record2:
             predictList.append(float(row[1]))
             predictedTime.append(str(row[3]))

        self.lastDate=predictedTimeReal[0]
        return predictList

    def testMonthly(self,sensorID,):
        predictList =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        clf = load('MLPDaily.joblib')
        obj2 = Connection(sensorID)
        year=1397
        month=11
        day=15
        date = datetime(year, month, day)



        for i in range(0, 15):
            predictList[i].append(self.getInputDataset(sensorID, 15 - i, i))
            print(self.lastDate)
            year=self.lastDate.split('-')[0]
            month=self.lastDate.split('-')[1]
            day=int(self.lastDate.split('-')[2])+i
            date=datetime(int(year),int(month),int(day))
            print(date)
            obj2.connectToDatabaseMonthly(float(clf.predict(predictList[i])), sensorID, date)


