#In this class we will connect to our database
#all you need is creat a database and give
# its username and password to this class here
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import datetime
sensor_id=200
date=datetime.datetime
class Connection:
    host=''
    database=''
    user=''
    password=''

    def __init__(self,sensor_id):
        self.sensor_id=sensor_id
        print('this object successfuly has created!')
    def connectToDatabaseHourly(self,energy, sensor_id, date):

        connection = 0
        cursor =0
        try:
           connection = mysql.connector.connect(host=self.host,
                                     database=self.database,
                                     user=self.user,
                                     password=self.password,
                                     charset='utf8',
                                     use_unicode=True
                                     )
           # sql_insert_query = """ INSERT INTO `sensor_type_c_hourly_datas_predict`
           #                        (`id`, `energy`, `sensor_id`, `time`) VALUES (1,0.333,25, %s)"""

           cursor = connection.cursor(prepared=True)
           sql_insert_query = """ INSERT INTO `sensor_type_c_hourly_datas_predict`
                                     ( `energy`, `sensor_id`, `time`) VALUES (%s,%s,%s)"""

           insert_tuple = (energy, sensor_id, date)
           result = cursor.execute(sql_insert_query, insert_tuple)
           connection.commit()
           print ("Record inserted successfully into python_users table")

        except mysql.connector.Error as error :
            connection.rollback() #rollback if any exception occured
            print("Failed inserting record into python_users table {}".format(error))
        finally:
                #closing database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def getTheLastRecord(self,sensor_id,numberOfDays):
        connection = 0
        cursor = 0
        try:
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password,
                                                 charset='utf8',
                                                 use_unicode=True
                                                 )
            cursor = connection.cursor(prepared=True)

            sql_select_Query ="""SELECT * FROM `sensor_type_c_hourly_datas` WHERE sensor_id=%s ORDER BY time DESC limit %s"""

            cursor.execute(sql_select_Query,(sensor_id,numberOfDays*24+23,))
            records = cursor.fetchall()
            #print(records)




        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed read record from python_users table {}".format(error))
        finally:
            # closing database connection.
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

        return (records)


    def connectToDatabaseMonthly(self,energy, sensor_id, date):
        connection = 0
        cursor =0
        try:
           connection = mysql.connector.connect(host=self.host,
                                     database=self.database,
                                     user=self.user,
                                     password=self.password,
                                     charset='utf8',
                                     use_unicode=True
                                     )
           # sql_insert_query = """ INSERT INTO `sensor_type_c_hourly_datas_predict`
           #                        (`id`, `energy`, `sensor_id`, `time`) VALUES (1,0.333,25, %s)"""

           cursor = connection.cursor(prepared=True)
           sql_insert_query = """ INSERT INTO `sensor_type_c_daily_datas_predict`
                                     ( `energy`, `sensor_id`, `time`) VALUES (%s,%s,%s)"""

           insert_tuple = (energy, sensor_id, date)
           result = cursor.execute(sql_insert_query, insert_tuple)
           connection.commit()
           print ("Record inserted successfully into python_users table")

        except mysql.connector.Error as error :
            connection.rollback() #rollback if any exception occured
            print("Failed inserting record into python_users table {}".format(error))
        finally:
                #closing database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def getTheLastRecordMonthly(self,sensor_id,numberOfdays):
        connection = 0
        cursor = 0
        try:
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password,
                                                 charset='utf8',
                                                 use_unicode=True
                                                 )
            cursor = connection.cursor(prepared=True)

            sql_select_Query ="""SELECT * FROM `sensor_type_c_daily_datas` WHERE sensor_id=%s ORDER BY time DESC limit %s"""

            cursor.execute(sql_select_Query,(sensor_id,numberOfdays,))
            records = cursor.fetchall()
            #print(records)




        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed read record from python_users table {}".format(error))
        finally:
            # closing database connection.
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

        return (records)


    def getTheLastRecordMonthlyPredicted(self,sensor_id,numberOfDays):
        connection = 0
        cursor = 0
        try:
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password,
                                                 charset='utf8',
                                                 use_unicode=True
                                                 )
            cursor = connection.cursor(prepared=True)

            sql_select_Query ="""SELECT * FROM `sensor_type_c_daily_datas_predict` WHERE sensor_id=%s ORDER BY time DESC limit %s"""

            cursor.execute(sql_select_Query,(sensor_id,numberOfDays,))
            records = cursor.fetchall()
            #print(records)




        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed read record from python_users table {}".format(error))
        finally:
            # closing database connection.
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

        return (records)


    def getListOfSensorID(self):
        connection = 0
        cursor = 0
        try:
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password,
                                                 charset='utf8',
                                                 use_unicode=True
                                                 )
            cursor = connection.cursor(prepared=True)

            sql_select_Query = """SELECT sensor_id FROM `sensor_type_c_daily_datas`"""

            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            # print(records)




        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed read record from python_users table {}".format(error))
        finally:
            # closing database connection.
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        return (records)
