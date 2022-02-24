from download_files import download
from tasks import perform
from sqlite import db_

# Download files from https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/

url1 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.enron.txt'
url2 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.kos.txt'
url3 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.nips.txt'
url4 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.nytimes.txt'
url5 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.pubmed.txt'

download = download(url1, url2, url3, url4, url5)
files = download.download_f()
print(files)

# list of filenames is stored in files
# files = ['vocab.enron.txt', 'vocab.kos.txt', 'vocab.nips.txt', 'vocab.nytimes.txt', 'vocab.pubmed.txt']

############ q1.- Try to find out a count of each and every word in a respective file and
                    # return a list of tuple with word and its respective count.#####################

count_words = perform(files)

for j in count_words.count():
    print("\n")
    # printing only first 20 values
    print(j[0:20])

########## q2- try to perform the reduce operation to get a count of all the words starting with same alphabets.

for j in count_words.count_letters():
    print(j[0:10])
    print("\n")

######## q3 = Try to filter out all the words from dataset .#############

print(count_words.filter_data())

####### Q4. = create a tuple set of all the records avaialble in all the five file and then store it in sqllite DB.


sqlite_db = db_(files)

# Connecting with database
db_name = 'bag_of_words.db'
db = sqlite_db.db_conn(db_name)

# Create Table
table_name = "vocab"
col_details = "enron text, kos text, nips text, nytim text, pubmed text"
cursor = sqlite_db.create_table(db, table_name, col_details)

a = []

for i in sqlite_db.open_file():
    a.append(i)

# records from each file
l1 = a[0]
l2 = a[1]
l3 = a[2]
l4 = a[3]
l5 = a[4]

# tuple set of all the records available in all the five file
lst = list(zip(l1, l2, l3, l4, l5))

# insert values into database
print(sqlite_db.insert_values(table_name, lst, cursor))

# Show data from database
print(sqlite_db.show(table_name, cursor))
