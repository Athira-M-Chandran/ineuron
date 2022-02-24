import logging
import sqlite3

# Create log
logging.basicConfig(filename='log.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class db_:
    def __init__(self, files):
        self.files = files

    def db_conn(self, db_name):
        '''
        connecting database
        :return: connection
        '''

        try:
            db = sqlite3.connect(db_name)
            logging.info("Connected successfully")
            return db

        except Exception as e:
            logging.error("Error Occurred while connecting to database: " + str(e))
            return "Error Occurred while connecting to database: ", e

    def create_table(self, db, table_name, col_details):
        '''
        create cursor object and table for database
        :param db: table name, db connectivity, column names with type
        :return: cursor object
        '''

        try:
            c = db.cursor()
            c.execute('create table ' + table_name + '(' + col_details + ' )')
            logging.info("Created Cursor object and table with columns Successfully ")
            return c
        except Exception as e:
            logging.error("Error Occurred while creating table : " + str(e))
            return "Error Occurred while creating table : ", e

    def open_file(self):
        '''
        Open files and Read records from each file
        :return: each records
        '''

        try:
            for i in self.files:
                with open(i, 'r', encoding="utf8") as f:
                    records = f.read().split('\n')
                    yield records
            logging.info("Read records successfully")
        except Exception as e:
            logging.error("Error Occurred while opening files : " + str(e))
            return "Error Occurred while opening files : ", e

    def insert_values(self, table_name, lst, cursor):
        '''
        insert lst(tuple set of all the records available in all the five file) into sqlite db
        :param table_name: table name to insert data
        :param lst: tuple set of all the records available in all the five file
        :param cursor: cursor object for execution db
        :return: success or not
        '''


        try:
            row = []
            for i in lst:
                for j in i:
                    row.append('"' + j + '"')
                    query = f'insert into {table_name} values({",".join(row)})'
                cursor.execute(query)
                row.clear()

            logging.info("Inserted Successfully")
            return "Inserted Successfully"

        except Exception as e:
            logging.error("Error Occurred while inserting values : " + str(e))
            return "Error Occurred while inserting values : ", e

    def show(self, table_name, cursor):
        '''
        Show data from table
        :param table_name: data fetch from this table name
        :param cursor: cursor object for execution
        :return: data from table
        '''

        try:
            data = cursor.execute('select * from ' + table_name + '')
            return data.fetchall()

        except Exception as e:
            logging.error("Error Occurred while fetching : " + str(e))
            return "Error Occurred while fetching : ", e
