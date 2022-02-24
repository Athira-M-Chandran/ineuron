
### TASK

Download last five files from Bag of words dataset - https://archive.ics.uci.edu/ml/datasets/Bag+of+Words

q1.- Try to find out a count of each and every word in a respective file return a list of tuple with word and its respective count.

sample example- [('sudh', 6),('kumar',3)]

q2- Try to perform the reduce opaertion to get a count of all the words starting with same alphabets.

sample eg - [('a', 56),(b, 34),(c,43),.......]

q3. - Try to filter out all the words from dataset

eg - .001.abstract = abstract

= .002 = delete

q4 - Create a tuple set of all the recored available in all 5 file and then store it in sqlite DB

eg. (aah, >= , 354, fdsf, wer)

#### TASK SUMMARY

**Modular coding**
**OOPS concept** is followed
**Exception Handling** is done
**Logging file** created

Contains 4 files:

1. **download_files.py** : 
        Download the files needed for the task
        
        :param args: urls passed from **main.py** as args
        
        :return: file names

2. **task.py** :

&nbsp;&nbsp;&nbsp;1 to 3 tasks from above is done in this file

&nbsp;&nbsp;&nbsp;q1. Try to find out a count of each and every word in a respective file return a list of tuple with word and its respective count.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used **counter module** for count, 
              
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For returning list of tuple used **zip()** and return values using generator **yield**
              
&nbsp;&nbsp;&nbsp;q2. Try to get a count of all the words starting with same alphabets.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For creating alphabet list used **string module**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and for returning values same as above **zip()** and **yield** is used

&nbsp;&nbsp;&nbsp;q3 Try to filter out all the words from dataset

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For checking each character used **isalpha()** from **string module**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return as string and first 300characters is returned using **slicing**

3. **sqlite.py** :


&nbsp;&nbsp;&nbsp; Task 4 is performed under this file since it contains database connection

&nbsp;&nbsp;&nbsp;q4 - Create a tuple set of all the recored available in all 5 file and then store it in sqlite DB

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**connecting sqlite3** and **create database**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**create table** with **column names** passed from **main.py**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Insert values** by Creating a tuple set of all the recored available in all 5 file from downloaded file which mentioned above
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Display** the same

4. **main.py** :

&nbsp;&nbsp;&nbsp;This file should be **executed**

##### Log file

![log](https://user-images.githubusercontent.com/86779388/155570452-190afdb1-a042-4e9b-ae92-34a5c5ce7c16.jpg)
