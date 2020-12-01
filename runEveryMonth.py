# OK so we wanna get the sensors:))
from ConnectDB import Connection
from test import Test

getSensorIDs = Connection(200)
sensorIDs = getSensorIDs.getListOfSensorID()
lenOfList = getSensorIDs.getListOfSensorID().__len__()
uniqueSensorIDs = []
uniqueSensorIDs.append(sensorIDs[0])
test = Test()
# o1.testMonthly(220)


for i in range(1, lenOfList):
    if sensorIDs[i] == sensorIDs[i - 1]:
        i += 1
    elif sensorIDs[i] != sensorIDs[i - 1]:
        uniqueSensorIDs.append(sensorIDs[i])
print(uniqueSensorIDs.__len__())

for i in range(0, uniqueSensorIDs.__len__()):
    test.testMonthly(int(uniqueSensorIDs[i][0]))


