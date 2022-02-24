import logging  # log creation
import requests  # downloading purpose

# Create log
logging.basicConfig(filename='log.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


# download files needed for the task

class download:

    def __init__(self, *args):

        self.args = args

    def download_f(self):
        '''
        Download the files needed for the task
        :param files: filenames
        :rtype: object
        :param args: path of files
        :return: file names
        '''
        logging.info("The files paths : " + str(self.args))
        try:
            file = []
            for i in self.args:
                r = requests.get(i, allow_redirects=True)
                open(i.split('/')[-1], 'wb').write(r.content)
                file.append(i.split('/')[-1])
            logging.info("Successfully Downloaded!")
            return file

        except Exception as e:
            logging.error("Error Occurred while downloading file : " + str(e))
            return "Error Occurred while downloading file : ", e

