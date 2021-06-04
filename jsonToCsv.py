import json
import csv
import os

class jsonToCsv:
    """
    Convert json files from ReelGood.com into one CSV file.
    """
    def __init__(self):
        pass

    def convert(self, website, showType, numShows, cwd):
        scrapedfiles = []
        for i in range(0, numShows, 50):
            fileBuilder = f"{cwd}/{website}-{showType}-{i}.json"
            scrapedfiles.append(fileBuilder)

        for eachfile in scrapedfiles:
            with open(eachfile) as jsonFile:
                myDict = json.load(jsonFile) # this is already a dictionary
                movieList = []
                for movieHash in myDict:
                    movieList.append(myDict[movieHash])

                
                with open(f"{website}-{showType}.csv", mode='a') as csvFile:
                    csvWriter = csv.writer(csvFile)

                    # If the csv file is empty, add a header
                    if os.stat(f"{website}-{showType}.csv").st_size == 0:
                        header = []
                        for k,v in movieList[0].items():
                            header.append(k)
                        csvWriter.writerow(header)

                    # Add every attribute for each movie in movie list.
                    for each in movieList:
                        tempList = []
                        for k,v in each.items():
                            tempList.append(v)

                        # Check for null rotten tomatoes rating at column 3
                        if not tempList[3].__class__ is int:
                            tempList.insert(3, "")

                        # Check for null classification at column 16
                        if tempList[16].__class__ is bool:
                            tempList.insert(16, "")
                        csvWriter.writerow(tempList)
                    
                    csvFile.close()
                jsonFile.close()





