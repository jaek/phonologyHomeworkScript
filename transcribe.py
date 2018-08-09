#!/bin/python


# CSV notes - 
# row[1] = ipa symbol
import csv
from fuzzywuzzy import fuzz


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def getDataFromCsv(FileName):
    data = {} 
    with open(FileName) as csvfile:
        rawdata = csv.reader(csvfile, delimiter=',')
        for row in rawdata:
            if(row[5] != ''):
                data[row[1]] = str(row[4]) + ' ' + str(row[5]) + ' ' + str(row[6])
            if(row[7] != ''):
                data[row[1]] = str(row[7]) + ' ' + str(row[8]) + ' ' + str(row[9])
    return data     

def searchData():
    fuzzfactor = 80
    while True:
        search = input("search for a phoneme : ")
        if (search == "q"):
            break
        if (RepresentsInt(search)):
            fuzzfactor = int(search)
        for key in data:
            if (fuzz.ratio(data[key], search) > fuzzfactor or key == search):
                print(key, data[key])

data = getDataFromCsv("ipa-data.csv")
searchData()
