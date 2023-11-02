#Ari Jacobs - s3958308

#Explain the concept of inheritance in programming. (15 to 25 words)
#Inheritence in programming refers to the mechanism that allows a class to use some aspects such as behaviours 
#and properties from another class. This allows for code to be reused and also establishes a relationship to an extent between the classes

from CAccount import CAccount
from SAccount import SAccount
from Customer import Customer

class bank:
    @staticmethod
    def main():
        fleet = []
        cAccounts = []
        sAccounts = []
        customers = []

        idx = 0

#open and read customer txt file
        fOpen = open("C:\\Users\\arija\\Desktop\\DIT\\Object oriented language\\Project 2\\Customers.txt", "r")

        for lines in fOpen:
            lines = lines.rstrip("\n")
            data = lines.split(' ; ')
            customer = Customer(int(data[0]), data[1], int(data[2]), data[3])
            Customer.append(Customer)

        fOpen.close()

#open and read cAccounts txt file
        fOpen = open("C:\\Users\\arija\\Desktop\\DIT\\Object oriented language\\Project 2\\CAccounts.txt", "r")
    
        for lines in fOpen:
            lines= lines.rstrip("\n")
            data = lines.split(' ; ')
            cAccount = CAccount(data[0], data[1], data[2])
            cAccount.append(CAccount)

        fOpen.close()

#Open and read sAccounts txt file
        fOpen = open("C:\\Users\\arija\\Desktop\\DIT\\Object oriented language\\Project 2\\SAccounts.txt", "r")

        for lines in fOpen:
            lines = lines.rstrip("\n")
            data = lines.split(' ; ')
            sAccountRead = SAccount(data[0], data[1], data[2])
            sAccount.append(SAccount)
#adds object to end of an existing list - Append
        fOpen.close()

        for cAccount in cAccount:
            print("\n Checking Account Details")
            print(cAccount)

        for sAccount in sAccount:
            print("\n Saving Account Details")
            print(sAccount)

        for customer in customer:
            print("\n Customer Details")
            print("Customer name: " + customer.getcustNm())

        for item in fleet:
            print("++++Bank details++++")
            item.cAccount()

        for item in fleet:
            print("++++Customer details++++")
            item.customer() 

         


        

