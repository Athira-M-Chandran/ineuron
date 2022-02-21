import logging as log

import pymongo
import csv

class mongodb:

    def __init__(self, connection_url, db_name, collection_name):
        self.connection_url = connection_url
        self.db_name = db_name
        self.collection_name = collection_name

    def connection(self):
        ''' Connecting with mongodb '''

        try:
            client = pymongo.MongoClient(self.connection_url)
            db = client.test
            log.info("Connection Successfull")
            return client

        except Exception as e:
            log.error("Error Occurred in connecting : " +str(e))
            return "Error Occurred in connecting : ",e

    def database_creation(self,client):
        ''' Database creation '''

        try:
            # Check whether database is already exists or not
            if self.db_name in client.list_database_names():
                log.info("database already exists : " +self.db_name )
                return "Database already exists"

            # else create one
            else :
                db = client[self.db_name]
                log.info("DB created successfully :" + self.db_name )
                return db

        except Exception as e:
            log.error("Error Occurred while creating database: " +str(e))
            return "Error Occurred while creating database : " ,e

    def create_collection(self,db):
        '''Collection Creation'''

        try:

            # check if collection already exists
            print(type(db))
            if self.collection_name in db.list_collection_names():
                log.info("Collection already exists : " + self.collection_name)
                return "Collection already exists"

            # Else create new one
            else:
                collection = db[self.collection_name]
                log.info("Collection created successfully :" + self.collection_name)
                return collection

        except Exception as e:
            log.error("Error Occurred while creating collection: " + str(e))
            return "Error Occurred while creating collection : ", e

    def insert_data(self,filename,collection):
        '''Insert bulk data; from csv file to database'''

        try:
            with open(filename, 'r') as data:
                reader = csv.DictReader(data, delimiter=';')
                for line in reader:
                    collection.insert_one(line)

            log.info("datas inserted successfully")
            return "Data inserted Successsfully"

        except Exception as e:
            log.error("Error Occurred while bulk data insertion :" +str(e) )
            return "Error Occurred while bulk data insertion :" , e

