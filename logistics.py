# Python terminal application to support logistics tracking of packages
# for SwollenHippo Logistics. All data is stored to an SQLite database
# Author: Garet Byrd
# Date Modified: 13 October 2026
import os
import sqlite3
from datetime import datetime, timezone
#Global variables and functions
datNow = datetime.now(timezone.utc)



strContinue = 1
while strContinue <= 5:
    strContinue = mainMenu()
    def mainMenu():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("SwollenHippo Logistics Package Tracking Support System\n")
        print("-------------------------------------------------------\n")
        print("MAIN MENU")
        print("----------\n")
        print("1. Create a new package shipment")
        print("2. View the shipping information for an existing package")
        print("3. Update the shipping information for an existing package")
        print("4. Delete an existing package")
        print("5. Record the arrival of a package at a regional shipping facility")
        print("6. Exit the application")
        print("-------------------------------------------------------\n")
        strChoice = input("Please select a menu item to continue (1-6)\n")

        if strChoice == "1":
            createPackage()
            return 1
        elif strChoice == "2":
            viewPackage()
            return 2
        elif strChoice == "3":
            updateDetails()
            return 3
        elif strChoice == 4:
            deletePackage()
            return 4
        elif strChoice == 5:
            updateTracking()
            return 5
        elif strChoice == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Thank you for using the SwollenHippo Logistics Package Tracking Support System")
            return 6
        else:
            return 0


# This is my create packages function
def createPackage(strTrackingNumber, strDestinationFirstName, strDestinationLastName, strDestinationCompany, strDestinationStreetAddress, strDestinationCity, strDestinationState, strDestinationZIPCode, strOriginatingCustomer, strOriginatingFacilityID):
    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conIndustries:
        strQuery =f"INSERT INTO customers VALUES (?,?,?,?,?,?,?,?,?,?)"
        tupValues = (strTrackingNumber, strDestinationFirstName, strDestinationLastName, strDestinationCompany, strDestinationStreetAddress, strDestinationCity, strDestinationState, strDestinationZIPCode, strOriginatingCustomer, strOriginatingFacilityID)
        objCursor = conIndustries.cursor()
        objCursor.execute(strQuery,tupValues)
        conIndustries.commit()
    conIndustries.close()

#This is my update packages function
def viewPackage(strTrackingNumber):
    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conIndustries:
        tupValues = (strTrackingNumber)
        objCursor = conIndustries.cursor()
        objCursor.execute(strTrackingNumber,tupValues)

        
    

def updateDetails(strTrackingNumber,strDestinationFirstName, strDestinationLastName, strDestinationCompany, strDestinationStreetAddress, strDestinationCity, strDestinationState, strDestinationZIPCode, strOriginatingCustomer, strOriginatingFacilityID):
    with  sqlite3.connect("SwollenHippoLogistics_Sample.db") as conIndustries:
        strQuery = f"UPDATE packages SET TrackingNumber = ?, DestinationFirstName = ?, DestinationLastName = ?, DestinationCompany = ?, DestinationStreetAddress = ?, DestinationCity = ?, DestinationZIPCode = ?, OriginatingCustomer = ?, OriginatingFacilityID = ?"
        tupValues = (strTrackingNumber,strDestinationFirstName, strDestinationLastName, strDestinationCompany, strDestinationStreetAddress, strDestinationCity, strDestinationState, strDestinationZIPCode, strOriginatingCustomer, strOriginatingFacilityID)
        objCursor = conIndustries.cursor()
        objCursor.execute(strQuery,tupValues)

        conIndustries.commit()
    conIndustries.close()



def deletePackage(strTrackingNumber):
    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conIndustries:
        strQuery = f"DELETE FROM packages TrackingNumber = ?"
        tupValues =(strTrackingNumber,)
        objCursor = conIndustries.cursor()
        print(tupValues)
        objCursor.execute(strQuery,tupValues)

        conIndustries.commit()
    conIndustries.close()
deletePackage()

#This is my review package function
def updateTracking(strTrackingNumber,strFacilityID, strCity, strState, strArrivalDateTime):
    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conIndustries:
        strQuery = f"UPDATE packages SET TrackingNumber = ?, FacilityID = ?, City = ?, State = ?"
        tupValues = (strTrackingNumber,strFacilityID, strCity, strState, strArrivalDateTime)
        objCursor = conIndustries.cursor()
        objCursor.execute(strQuery,tupValues)

        conIndustries.commit()
    conIndustries.close()

def checkIfPackageExists(strTrackingNumber):
    strQuery = "SELECT * FROM Packages WHERE TrackingNumber = ?"
    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conIndustries:
        objCursor = conIndustries.cursor()
        objCursor.execute(strQuery,strTrackingNumber)
        lstRows = objCursor.fetchall()
        conIndustries.close()
        if len(lstRows) >0:
            return True
        else:
            return False
        