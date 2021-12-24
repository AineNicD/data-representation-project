# deals with sql connector, functions for tables data, recipient and vaccinator. 

import mysql.connector
import dbconfig as cfg


class RecipientDao:

    db = ""

    def __init__(self):

        # Connect to Database
        self.db = mysql.connector.connect(host=cfg.mysql['host'],
                                          user=cfg.mysql['user'],
                                          password=cfg.mysql['password'],
                                          database=cfg.mysql['database'],
                                          port='3306')

# Create new recipient 
    def create(self, recipient):
        cursor = self.db.cursor()
        sql = "insert into recipients (id,firstname, surname, vaccine) values (%s,%s,%s,%s)"
        values = [
            recipient['id'], recipient['firstname'], recipient['surname'],
            recipient['vaccine']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid

# Get all the recipients 
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from recipients'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        cursor.close()
        return returnArray

# Find a recipient by id
    def findById(self, id):
        cursor = self.db.cursor()
        sql = 'select * from recipients where id = %s'
        values = [id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDict(result)

# Update a recipient
    def update(self, recipient):
        cursor = self.db.cursor()
        sql = "update recipients set firstname = %s, surname = %s, vaccine = %s where id = %s"
        values = [
            recipient['firstname'], recipient['surname'],
            recipient['vaccine'], recipient['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return recipient

# Delete a recipient
    def delete(self, id):
        cursor = self.db.cursor()
        sql = 'delete from recipients where id = %s'
        values = [id]
        cursor.execute(sql, values)

        cursor.close()
        return {}

# Convert a list to dictionary
    def convertToDict(self, result):
        colnames = ['id', 'firstname', 'surname', 'vaccine']
        recipient = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                recipient[colName] = value

        return recipient


recipientDao = RecipientDao()


class VaccinatorDao:
    db = ""

    def __init__(self):
             # Connect to Database
        self.db = mysql.connector.connect(host=cfg.mysql['host'],
                                        user=cfg.mysql['user'],
                                        password=cfg.mysql['password'],
                                        database=cfg.mysql['database'],
                                        port='3306')    
    

# Create new vaccinator 
    def createVaccinator(self, vaccinator):
        cursor = self.db.cursor()
        sql = "insert into vaccinators (reg_no, firstname, surname, profession) values (%s,%s,%s,%s)"
        values = [
            vaccinator['reg_no'], vaccinator['firstname'], vaccinator['surname'],
            vaccinator['profession']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid

# Get all the vaccinators
    def getAllVaccinator(self):
        cursor = self.db.cursor()
        sql = 'select * from vaccinators'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        cursor.close()
        return returnArray

# Find a specific vaccinator by reg_no
    def findByReg(self, reg_no):
        cursor = self.db.cursor()
        sql = 'select * from vaccinators where reg_no = %s'
        values = [reg_no]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDict(result)

# Update a vaccinator
    def updateVaccinator(self, vaccinator):
        cursor = self.db.cursor()
        sql = "update vaccinators set firstname = %s, surname = %s, profession = %s where reg_no = %s"
        values = [
            vaccinator['firstname'], vaccinator['surname'],
            vaccinator['profession'], vaccinator['reg_no']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return vaccinator

# Delete a vaccinator
    def deleteVaccinator(self, reg_no):
        cursor = self.db.cursor()
        sql = 'delete from vaccinators where reg_no = %s'
        values = [reg_no]
        cursor.execute(sql, values)

        cursor.close()
        return {}

 #Convert a list to dictionary
    def convertToDict(self, result):
        colnames = ['reg_no', 'firstname', 'surname', 'profession']
        vaccinator = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                vaccinator[colName] = value

        return vaccinator


vaccinatorDao = VaccinatorDao()