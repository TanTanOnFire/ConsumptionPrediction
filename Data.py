#In this class, firstly we will read an file named: HourlyUsageReport
#then we will generate 24 file which consist of weight for prediction
#for usage of this file: first you should export database as a csv file
#then you can run file named: train.py
#these two file can be used monthy or less because there's no need to update weight
#everyday. This action should be done by admin:)
import csv

class ReadingData:
    hour= 0
    hour1=0
    x_train = []
    y_train = []
    counter = 0
    numberOfHour = 1
    numberOfLayer=1
    intHour=0
    x_train_h1 = []
    y_train_h1 = []
    x_train_h2 = []
    y_train_h2 = []
    x_train_h3 = []
    y_train_h3 = []
    x=[]

    def calculateForMonth(self):
        with open('sensor_type_c_daily_datas_predict.csv') as file:
            reader = csv.reader(file,delimiter=',')
            for row in reader:
                print(row[1],row[2])


    def threeHour(self,input_count,output_count,hour,numOfDays):
        i=0

        h=int(hour)
        stringHour2=str(h+1)
        stringHour3 =str(h - 1)
        if h==10:
            stringHour3='0'+ str(h - 1)
        elif h==0:
            stringHour3='23'
            stringHour2='01'
        elif h==9:
            stringHour2='08'
            stringHour3='10'
        if 0<h<9:
            stringHour2 = '0' + str(h + 1)
            stringHour3 = '0' + str(h - 1)
        y = []
        energyInHour1 = []
        energyInHour2 = []
        energyInHour3 = []
        energyInHour = []

        with open("HourlyUsageReport.csv") as file:
            reader = csv.reader(file, delimiter=',')
            nh = int((2 / 3) * input_count + output_count)
            self.numberOfLayer=nh

            for row in reader:
                if row[2] == hour:
                    energyInHour1.append(float(row[0]))


                if row[2]== stringHour2:
                    energyInHour2.append(float(row[0]))

                if row[2]== stringHour3:
                    energyInHour3.append(float(row[0]))
            temp1=[]
            temp2=[]
            temp3=[]

            for i in range (i,numOfDays):
                temp1.append(energyInHour1[i])
                temp2.append(energyInHour2[i])
                temp3.append(energyInHour3[i])


            y.append(energyInHour1[numOfDays])
            y.append(energyInHour2[numOfDays])
            y.append(energyInHour3[numOfDays])
            energyInHour.append(temp1)
            energyInHour.append(temp2)
            energyInHour.append(temp3)
            #print(energyInHour)
            self.x_train_h1=energyInHour
            self.y_train_h1=y

    def calculate(self, input_count,output_count,hour):
        self.intHour= int(hour)
        with open("HourlyUsageReport.csv") as file:
            reader = csv.reader(file, delimiter=',')
            y = []
            x = []
            nh = int((2 / 3) * input_count + output_count)
            self.numberOfLayer=nh
            energyInHour = []
            temp = []
            for row in reader:
                if row[2] == hour:
                    energyInHour.append(float(row[0]))

            index = 0
            # for i in energyInHour:
            #     print("energyInHour[{}] = {}".format(index, i))
            #     index += 1
            count = 0
            #tempX = []
            p = 0

            while count < output_count:
                tempX = self.inputData(p, input_count, energyInHour)
                x.append(tempX)
                y.append(energyInHour[p + input_count])
                p += 1
                count += 1

        self.x_train=x
        self.y_train=y
        #print(self.x_train)

    def inputData(self,p, ic, arr):
        temp = []
        for i in range(p, p + ic):
            temp.append(arr[i])
        return temp

    def getX(self,input_count,output_count,hour):
        self.intHour = int(hour)
        with open("HourlyUsageReport.csv") as file:
            reader = csv.reader(file, delimiter=',')
            y = []
            x = []
            nh = int((2 / 3) * input_count + output_count)
            self.numberOfLayer = nh
            energyInHour = []
            temp = []
            for row in reader:
                if row[2] == hour:
                    energyInHour.append(float(row[0]))

            index = 0
            # for i in energyInHour:
            #     print("energyInHour[{}] = {}".format(index, i))
            #     index += 1
            count = 0
            # tempX = []
            p = 0

            while count < output_count:
                tempX = self.inputData(p, input_count, energyInHour)
                x.append(tempX)
                y.append(energyInHour[p + input_count])
                p += 1
                count += 1

        self.x_train = x
        return self.x_train

    def getY(self,input_count,output_count,hour):
        self.intHour = int(hour)
        with open("HourlyUsageReport.csv") as file:
            reader = csv.reader(file, delimiter=',')
            y = []
            x = []
            nh = int((2 / 3) * input_count + output_count)
            self.numberOfLayer = nh
            energyInHour = []
            temp = []
            for row in reader:
                if row[2] == hour:
                    energyInHour.append(float(row[0]))

            index = 0
            # for i in energyInHour:
            #     print("energyInHour[{}] = {}".format(index, i))
            #     index += 1
            count = 0
            # tempX = []
            p = 0

            while count < output_count:
                tempX = self.inputData(p, input_count, energyInHour)
                x.append(tempX)
                y.append(energyInHour[p + input_count])
                p += 1
                count += 1

        self.y_train = y
        return self.y_train

    def getNH(self,input_count,output_count):
        nh = int((2 / 3) * input_count + output_count)
        return nh

    def getXH1(self,input_count,output_count):
        #self.intHour = int(hour)
        with open("sensor_type_c_daily_datas_predict.csv") as file:
            reader = csv.reader(file, delimiter=',')
            y = []
            x = []
            nh = int((2 / 3) * input_count + output_count)
            self.numberOfLayer = nh
            energyInHour = []
            temp = []
            for row in reader:
                energyInHour.append(float(row[1]))

            index = 0
            # for i in energyInHour:
            #     print("energyInHour[{}] = {}".format(index, i))
            #     index += 1
            count = 0
            # tempX = []
            p = 0

            while count < output_count:
                tempX = self.inputData(p, input_count, energyInHour)
                x.append(tempX)
                y.append(energyInHour[p + input_count])
                p += 1
                count += 1

        self.x_train_h1 = x
        #return self.x_train

        return self.x_train_h1

    def getYH1(self,input_count,output_count):
        with open("sensor_type_c_daily_datas_predict.csv") as file:
            reader = csv.reader(file, delimiter=',')
            y = []
            x = []
            nh = int((2 / 3) * input_count + output_count)
            self.numberOfLayer = nh
            energyInHour = []
            temp = []
            for row in reader:
                energyInHour.append(float(row[1]))

            index = 0
            # for i in energyInHour:
            #     print("energyInHour[{}] = {}".format(index, i))
            #     index += 1
            count = 0
            # tempX = []
            p = 0

            while count < output_count:
                tempX = self.inputData(p, input_count, energyInHour)
                x.append(tempX)
                y.append(energyInHour[p + input_count])
                p += 1
                count += 1

        self.y_train_h1 = y
        # return self.x_train

        return self.y_train_h1

# rd=ReadingData()
# rd.calculateForMonth()
#
# # listx=rd.getXH1(15,5)
# # listPR=rd.getXH1(15,1)
# # listy=rd.getYH1(15,5)
# # print(listx)
# # print(listy)
# # print(listPR)
# # nh=7
# # clf=MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(nh,), random_state=1, activation='relu')
# # clf.fit(listx,listy)
# # print(clf.predict(listPR))
# #
