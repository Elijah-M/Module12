"""
Author: Elijah Morishita
elmorishita@dmacc.edu
11/9/2020
This program imports data from the Iowa 2010 Census Data
Population Income spreadsheet, and them manipulates the data
"""
import csv


class IowaCensusData:

    def __init__(self, rank, county, per_capita_income, median_family_income, population, num_households):
        self.rank = rank
        self.county = county
        self.per_capita_income = per_capita_income
        self.median_family_income = median_family_income
        self.population = population
        self.num_households = num_households

    def readIowaFile(self):
        with open('Iowa2010Census.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            county = {}
            for row in csv_reader:
                # skips the first line in the file because it is the header
                if line_count == 0:
                    line_count += 1
                    continue
                # creates an item in dictionary county with a key of the county name and a value of the object
                county[str(row[0])] = IowaCensusData(row[1], row[2], row[3], row[4], row[5], row[6])
            county.pop('', None)  # This removes the blank 'Iowa State' key
            for x in county:
                print(county[x])

            total = sum(self.population)
            print("Total Iowa population: ", total)


        return county

    def __str__(self):
        return self.rank + self.county + self.per_capita_income + self.median_family_income + self.population + self.num_households


    def population_household(self, county):

        if list(county.keys())[list(county.values()).index('Dallas')]:
            list(county.keys())[list(county.values()).index('Dallas')]


# Define
IowaCensusDataInfo = IowaCensusData('', '', '', '', '', '')
IowaCensusDataInfo.readIowaFile()
IowaCensusDataInfo.population_household(IowaCensusDataInfo.readIowaFile())


# Garbage collection
del IowaCensusDataInfo
