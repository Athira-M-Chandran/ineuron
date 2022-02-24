import logging
# for count(self) ; Counter
from collections import Counter
# for count_letters(self); alpha_list
import string

# Create log
logging.basicConfig(filename='log.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class perform:

    def __init__(self, files):
        '''
        initialize filenames
        :param files: files
        '''

        self.files = files

    def count(self):
        '''
        count of each and every word in a respective file
        :return: a list of tuple with word and its respective count.
        '''

        try:
            for i in self.files:
                f = open(i, 'r', encoding="utf8")
                lst = f.read().split('\n')
                count = Counter(lst)
                yield list(zip(count.keys(), count.values()))
            logging.info("Count task performed and tuple with word and count returned!")
        except Exception as e:
            logging.error("Error Occurred while performing count operation : " + str(e))
            return "Error Occurred while performing count operation : ", e

    def count_letters(self):
        '''
        to get a count of all the words starting with same alphabets.
        :return: list of tuples with letter and count
        '''

        try:
            count = 0
            d = {}
            alpha_list = string.ascii_lowercase
            for i in self.files:
                f = open(i, 'r', encoding="utf8")
                lst = f.read().split('\n')

                for k in alpha_list:
                    count = 0
                    for j in lst:
                        if j.startswith(k):
                            count += 1

                    d.update([(k, count)])
                yield list(zip(d.keys(), d.values()))
            logging.info("list of tuples with alphabets and count returned!")
        except Exception as e:
            logging.error("Error occurred while performing alphabets and count : " + str(e))
            return "Error occurred while performing alphabets and count : ", e

    def filter_data(self):
        '''
        Try to filter out all the words from dataset .
        :return: words only no special characters
        '''

        try:
            new_words = ''
            for i in self.files:
                with open(i, 'r', encoding="utf8") as f:
                    lst = f.read().split('\n')
                for k in lst:
                    for j in k:
                        if j.isalpha():
                            new_words += j

                    new_words += ','
            logging.info("Filter out words from dataset")
            return new_words[0:300]

        except Exception as e:
            logging.error("Error occurred while filtering" + str(e))
            return "Error occurred while filtering", e
