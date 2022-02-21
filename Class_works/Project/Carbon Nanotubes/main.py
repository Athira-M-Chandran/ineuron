
import logging as log

from download_dataset import download_dataset
from mongodb_connection import mongodb
from operations import operation


# Create log

log.basicConfig(filename='log.log', level=log.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# Download dataset
path = "https://archive.ics.uci.edu/ml/machine-learning-databases/00448/carbon_nanotubes.csv"
filename = "carbon_nanotubes.csv"
obj = download_dataset(path, filename)
obj.download()

# Display top 10 datas
print(obj.show())

# Mongo db connection
connection_url = "mongodb+srv://mongodb:mongodb@cluster0.qjmki.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
db_name = 'Carbon_nano'
collection_name = 'carbon_data'

conn = mongodb(connection_url, db_name, collection_name)

# Database Connection
client = conn.connection()

# Database Creation
db = conn.database_creation(client)

# Collection Creation
collection = conn.create_collection(db)


# Insert data from filename
print(conn.insert_data(filename,collection))


######## Operations #############

# 1. Insertion
    # a. insert_one  ( as dictionary)
    # b. insert_many ( as list )

# Creating object
operations = operation(collection)

# a. insert_one  ( as dictionary)
dict1 = {
    "Chiral indice n" : "20",
    "Chiral indice m" : "7",
    "Initial atomic coordinate u" : "0,717300",
    "Initial atomic coordinate v" : "0,700129",
    "Initial atomic coordinate w" : "0,121319",
    "Calculated atomic coordinates u'" : "0,678414",
    "Calculated atomic coordinates v'" : "0,55675",
    "Calculated atomic coordinates w'" : "0,132369"
}

print(operations.insert_one(dict1))

# b. insert_many ( as list )
dict2 = [
    {
        "Chiral indice n": "14",
        "Chiral indice m": "9",
        "Initial atomic coordinate u": "0,617300",
        "Initial atomic coordinate v": "0,600129",
        "Initial atomic coordinate w": "0,101319",
        "Calculated atomic coordinates u'": "0,578414",
        "Calculated atomic coordinates v'": "0,45675",
        "Calculated atomic coordinates w'": "0,102369"
    },
    {
        "Chiral indice n": "20",
        "Chiral indice m": "7",
        "Initial atomic coordinate u": "0,517300",
        "Initial atomic coordinate v": "0,600129",
        "Initial atomic coordinate w": "0,111319",
        "Calculated atomic coordinates u'": "0,578414",
        "Calculated atomic coordinates v'": "0,45675",
        "Calculated atomic coordinates w'": "0,112369"
    },
    {
        "Chiral indice n": "15",
        "Chiral indice m": "11",
        "Initial atomic coordinate u": "0,417300",
        "Initial atomic coordinate v": "0,600129",
        "Initial atomic coordinate w": "0,101319",
        "Calculated atomic coordinates u'": "0,578414",
        "Calculated atomic coordinates v'": "0,45675",
        "Calculated atomic coordinates w'": "0,122369"
    }

]

print(operations.insert_many(dict2))

## 2. UPDATE OPERATION
    # a. Update one record
    # b. Update many records

# a. Update one record
update_one_data = {
                      "Chiral indice n": "15"
                  },\
                  {
                      "$set" : {
                          "Calculated atomic coordinates w'" : "0,100000"
                      }
                  }
print(operations.update_one(update_one_data))

# b. Update many record
update_many_data = {
                       "Chiral indice n" : {'$gte' : '20'}
                   },\
                   {
                       '$set' : {"Chiral indice n" : '18'}
                   }
print(operations.update_many(update_one_data))

## Fetch / Read records

        # a. Fetch all data
        # b. Fetch One data
        # c. Fetch data with condition
        # d. Fetch using 'in' condition
        # e. Fetch records with limit

# a. Fetch all data
for j in operations.fetch_all():
    print(j)

# b. Fetch one data
print(operations.fetch_one())

# c. Fetch data with condition
condition = {"Chiral indice n" : "13"}
for j in operations.fetch_condition(condition):
    print(j)

# d. Fetch data with in operator
condition1 = {"Chiral indice n" :{"$in" : ['13' , '14' , '18','20']}, 'Chiral indice m': '7'}
for j in operations.fetch_in(condition1):
    print(j)

# e. Fetch records with limit
limit = 2
for j in operations.fetch_limit(limit):
    print(j)

######### Filter Operation #########
        # $gt - greater than
        # $gte - greater than or equal to
        # $lt - lesser than
        # $lte - lesser than or equal to
        # $ne - Not equal to
        # $and - Logic AND
        # $or - Logic OR
        # $not - Logic NOT

# filter using $gte
condition_gte = {'Chiral indice n' : {"$gte" : "14"}}
for j in operations.filter_gte(condition_gte):
    print(j)

# filter using not $lt
condition_not = {'Chiral indice n': {'$not': {'$lt': '17'}}}
for j in operations.filter_not(condition_not):
    print(j)

############# DELETION ############
        # a. delete one
        # b. delete many
# delete one
condition_del_one = {'Chiral indice n': '14'}
print(operations.delete_one(condition_del_one))

# b. delete many
condition_del_many = {'Chiral indice n': '11'}
print(operations.delete_many(condition_del_many))

# c. drop
print(operations.drop())