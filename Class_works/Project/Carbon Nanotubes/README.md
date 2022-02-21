### TASK

#### 1. Visit link https://archive.ics.uci.edu/ml/datasets/Carbon+Nanotubes
#### 2. Download the dataset
#### 3. Insert data from dataset to mongodb (bulk insertion)
#### 4. Different operations

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **4a. Insertion**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **4b. Update**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **4c. Find Operation**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **4d. Filter Operation**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **4e. Deletion**

### Code Evaluation

#### 1. Modular coding
#### 2. Exception Handling
#### 3. Proper log

### Project Summary

#### Done with 4 files

1. **download_dataset.py** - This file contains function to download dataset and called from  **main.py**
2. **mongodb_connection.py** - This file contains connection related function and called from **main.py**
3. **operations.py** - This file contains all the operations (Task No.4 from above) and called from **main.py**
                      
                      4a. Insertion - 
                              insert_one
                              insert_many
                      
                      4b. Update-
                              find_one_and_update
                              update_many
                      
                      4c. Find - 
                              Fetch all data
                              Fetch One data
                              Fetch data with condition
                              Fetch using 'in' condition
                              Fetch records with limit
                              
                      4e.Filter Operation 
                              $gt - greater than
                              $gte - greater than or equal to
                              $lt - lesser than
                              $lte - lesser than or equal to
                              $ne - Not equal to
                              $and - Logic AND
                              $or - Logic OR
                              $not - Logic NOT
                              
                      4d. Delete
                              delete_one
                              delete_many
                              drop

4. **main.py** - Master file

**Exception handling** and **logging** also done 

