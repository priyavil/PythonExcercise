#StarWars.py
import logging
import requests
import csv
import os

#This is developed on Python version 3.6 and windows 
#Decorator implementation for logging
class logger(object):
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)

    def printArguments(func):
        '''Decorator to print function call details - parameters names and effective values'''
        def wrapper(*func_args, **func_kwargs):
            var = len(func_args) -1
            logging.debug('Start func: {}'.format(func.__name__))
            logging.debug( "Total number of arguments : {} " .format(var))
            for index in range(1, len(func_args),1):
                logging.debug ("Arguments {0} value : {1}" .format(index, func_args[index]))
            return func(*func_args, **func_kwargs)
        return wrapper

#APIHelper class responsible to retieve the data using HTTP 
# and parse the json file to store it into the list
class ApiHelper(logger):

    @logger.printArguments
    def star_wars_characters(self, page_nr):
        try: 
            #url = "https://swapi.co/api/people/"
            r = requests.get(page_nr)
            return self.parseJson(r.json())
        except:
            logging.debug ("Unexpected error: cannot proceed further")
            raise


    def parseJson(self, jsonres):
        listOfList = []
        a_list = jsonres["results"]
        for item in a_list:
            name = item['name']
            height = item['height']
            gender = item['gender']
            listtemp = []
            listtemp.append(name)
            listtemp.append(height)
            listtemp.append(gender)
            listOfList.append(listtemp)
            #print("name: " + name, "height : " + height, "gender: " + gender )

        return listOfList

    #arguments - send list of names , height and gender, no need to call the method multiple times 
    #so we are changing the signature of the method
    def append_to_file(self,path, listOfList):
        headers = ['Name', 'Height', 'Gender']
        with open(path, 'a+') as myfile:
            writer = csv.writer(myfile)
            for item in listOfList:
                writer.writerow(item)
            myfile.close()




class api(logger):
    @logger.printArguments
    def sample(self,hi):
        print(hi)

def main():
    try:
        url = "https://swapi.co/api/people/"
        obj = ApiHelper()
        listOfList = obj.star_wars_characters(url)
        #send file name for CSV file 
        path = "filename.csv"
        obj.append_to_file(path,listOfList )
    except:
        print("Caught it!")

  
if __name__== "__main__":
  main()