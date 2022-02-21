import requests
import logging as log
import pandas as pd


class download_dataset:

    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
        log.info("dataset path is :" + path)

    def download(self):
        try:
            r = requests.get(self.path, allow_redirects=True)
            open(self.filename, 'wb').write(r.content)
            log.info("Download done and stored in " + self.filename)

        except Exception as e:
            log.error("Error Occurred : " + str(e))
            return e

    def show(self):

        try:
            data = pd.read_csv(self.filename, delimiter=';')
            log.info("Data displayed successfully")
            return data.head(10)


        except Exception as e:
            log.error("Error Occurred in show : " + str(e))
            return "Error Occurred in display data : ", e
