import logging as log

class operation:
    ''' To perform various database operation '''
    log.info("\n\n Operations \n")

    def __init__(self,collection):
        self.collection = collection


    def insert_one(self,dict1):
        ''' Inserting one set of value '''
        try:
            self.collection.insert_one(dict1)
            log.info("One data inserted successfully")
            return "One data inserted successfully"

        except Exception as e:
            log.error("Error Occurred while inserting one data : " +str(e))
            return "Error Occurred while inserting one data : " , e

    def insert_many(self,dict2):
        ''' Insert many data '''

        try:
            self.collection.insert_many(dict2)
            log.info("Many data inserted successfully")
            return "Many data inserted successfully"

        except Exception as e:
            log.error("Error Occurred while inserting many data : " + str(e))
            return "Error Occurred while inserting many data : " , e

    def update_one(self,update_one_data):
        ''' Update one data from dataset '''

        try:
            self.collection.find_one_and_update(update_one_data)
            log.info("Updated one data successfully")
            return "Updated one data successfully"

        except Exception as e:
            log.error("Error Occurred while updating single data : " +str(e))
            return "Error Occurred while updating single data : ",e

    def update_many(self, update_many_data):
        ''' Update many data of dataset '''

        try:
            self.collection.update_many(update_many_data)
            log.info("Updated one data successfully")
            return "Updated one data successfully"
        except Exception as e:
            log.error("Error Occurred while updating many data : " + str(e))
            return "Error Occurred while updating many data : ", e

    def fetch_all(self):
        ''' Fetch all data '''

        try:
            for i in self.collection.find():
                yield i
            log.info("Fetch all data successfully!")

        except Exception as e:
            log.error("Error Occurred while fetching all data : " + str(e))
            return "Error Occurred while fetching all data : ", e


    def fetch_one(self):
        ''' Fetch One data '''

        try:
            data = self.collection.find_one()
            log.info("One data fetched successfully : " +str(data))
            return data
        except Exception as e:
            log.error("Error Occurred while fetching one data : " + str(e))
            return "Error Occurred while fetching one data : ", e

    def fetch_condition(self,condition):
        ''' Fetch data with condition'''

        try:
            for i in self.collection.find(condition):
                yield i
            log.info("Fetched data with condition!")
        except Exception as e:
            log.error("Error Occurred while fetching data with condition : " + str(e))
            return "Error Occurred while fetching data with condition : ", e

    def fetch_in(self,condition1):
        ''' Fetch data using in operator'''

        try:
            for i in self.collection.find(condition1):
                yield i
            log.info("Fetched data using in operator")

        except Exception as e:
            log.error("Error Occurred while fetching data with in operator : " + str(e))
            return "Error Occurred while fetching data with in operator : ", e

    def fetch_limit(self,limit):
        '''Fetch data using limit'''

        try:
            for i in self.collection.find().limit(limit):
                yield i
            log.info("Fetched data using limit!")
        except Exception as e:
            log.error("Error Occurred while fetching data with limit : " + str(e))
            return "Error Occurred while fetching data with limit : ", e

    def filter_gte(self,condition_gte):
        ''' Filter data greater than or equal to condition'''

        try:
            for i in self.collection.find(condition_gte):
                yield i
            log.info("Filter data with greater than or equal to condition")
        except Exception as e:
            log.error("Error Occurred while filtering data with greater than or equal to condition : " + str(e))
            return "Error Occurred while filtering data with greater than or equal to condition : ", e

    def filter_not(self,condition_not):
        ''' Filter condition not less than condition'''

        try:
            for i in self.collection.find(condition_not):
                yield i
            log.info("Filtered data successfully")

        except Exception as e:
            log.error("Error Occurred while filtering data with not less than condition : " + str(e))
            return "Error Occurred while filtering data with not less than condition : ", e

    def delete_one(self, condition_del_one):
        ''' Delete only one record'''

        try:
            self.collection.delete_one(condition_del_one)
            log.info("Deleted Successfully!")
            return "Deleted Successfully!"

        except Exception as e:
            log.error("Error occurred while deleting one record : " + str(e))
            return "Error occurred while deleting one record : ", e

    def delete_many(self,condition_del_many):
        ''' Delete many records'''

        try:
            self.collection.delete_many(condition_del_many)
            log.info("Many records deleted successfully!")
            return "Many records deleted successfully!"

        except Exception as e:
            log.error("Error occurred while deleting many record : " + str(e))
            return "Error occurred while deleting many record : ", e

    def drop(self):
        '''Drop collection'''

        try:
            self.collection.drop()
            log.info("Collection dropped successfully")
            return "Collection dropped successfully"

        except Exception as e :
            log.error("Error Occurred while dropping the collection : " + str(e))
            return "Error Occurred while dropping the collection : ", e