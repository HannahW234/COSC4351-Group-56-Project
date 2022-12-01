from table import *

def addToFile(diner, listOfTables, clientTable : Table, clientName):
    with open(f"dinerNotification/{diner}.txt", "a") as file:
        file.write(f"Client Name: {clientName} ")
        file.write(f"Reservation Date: {clientTable.date} ")
        file.write(f"Reservation Time: {str(clientTable.time)} ")
        file.write(f"Tables Combined: {str(listOfTables)} \n\n")

    file.close()

