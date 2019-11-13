# PythonExcercise
Python excercise

Settings
-------------
To run this program we need following setting,
Python Version 3.6
I developed this program on windows using VS
Need to install Request package if it is not installed using the following command 
to install request 

on windows : 
py -m pip install requests

On Ubuntu : 
pip install requests


To run the program :
------------------------

Go to the StarWars.py file 
Run StarWars.py file to get the csv(filename.csv) file in the current folder. 

1.StarWars chearacter retrieval : 
- Need to pass the pasge url for getting the character list
def star_wars_characters(page_nr) 

2. convert to csv file handled by 

 def append_to_file(self,path, listOfList):
 
 this will create list form the response from previous call
 
 3.Unit test added to check empty list 
 To run unit test, 
 Run StarWarsTest.py file
 it has a test method as test_nonEmptyArray to check whether we get empty list or not 
 
 4.ReadMe file added
 
 5. Logger class added to enable logging for this class using decorator 
 which will help us to log the name of method and their arguments
 
