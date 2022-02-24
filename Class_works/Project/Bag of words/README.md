
### TASK

Download last five files from Bag of words dataset - https://archive.ics.uci.edu/ml/datasets/Bag+of+Words

**q1.- Try to find out a count of each and every word in a respective file return a list of tuple with word and its respective count.** <br />
sample example- [('sudh', 6),('kumar',3)]

**q2- Try to perform the reduce opaertion to get a count of all the words starting with same alphabets.** <br />
sample eg - [('a', 56),(b, 34),(c,43),.......]

**q3. - Try to filter out all the words from dataset** <br />
eg - .001.abstract = abstract <br />
= .002 = delete

**q4 - Create a tuple set of all the recored available in all 5 file and then store it in sqlite DB** <br />
eg. (aah, >= , 354, fdsf, wer)

#### TASK SUMMARY

**Modular coding** <br />
**OOPS concept** is followed <br />
**Exception Handling** is done <br />
**Logging file** created <br />

Contains 4 files:


1. **download_files.py** : 

&nbsp; &nbsp; &nbsp; Download the files needed for the task <br />
  &nbsp; &nbsp; &nbsp; - parameter- args: urls passed from **main.py** as args <br />
  &nbsp; &nbsp; &nbsp; - return: file names


2. **task.py** :

&nbsp; &nbsp; &nbsp; 1 to 3 tasks from above is done in this file

&nbsp; &nbsp; &nbsp;  q1. Try to find out a count of each and every word in a respective file return a list of tuple with word and its respective count. <br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  - Used **counter module** for count, <br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  - For returning list of tuple used **zip()** and return values using generator **yield**
              
&nbsp; &nbsp; &nbsp;  q2. Try to get a count of all the words starting with same alphabets. <br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  - For creating alphabet list used **string module** <br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  - and for returning values same as above **zip()** and **yield** is used

&nbsp; &nbsp; &nbsp;  q3 Try to filter out all the words from dataset <br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  - For checking each character used **isalpha()** from **string module** <br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  - Return as string and first 300characters is returned using **slicing**


3. **sqlite.py** :


&nbsp; &nbsp; &nbsp; Task 4 is performed under this file since it contains database connection

&nbsp; &nbsp; &nbsp;  q4 - Create a tuple set of all the recored available in all 5 file and then store it in sqlite DB <br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  - **connecting sqlite3** and **create database** <br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  - **create table** with **column names** passed from **main.py** <br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  - **Insert values** by Creating a tuple set of all the recored available in all 5 file from downloaded file which mentioned above <br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  - **Display** the same


4. **main.py** :


&nbsp; &nbsp; &nbsp;  This file has to be **executed**


##### Log file

A part of logging file is shown below:

![log](https://user-images.githubusercontent.com/86779388/155570452-190afdb1-a042-4e9b-ae92-34a5c5ce7c16.jpg)
