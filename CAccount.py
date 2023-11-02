class CAccount:                                         #Ari Jacobs - S3958308
    bsbNumber = 1246

    def __init__(self, accNo, accType, bal , minAmt = 50.00):
        self.__accNo = accNo
        self.__accType = accType
        self.__bal = bal
        self.__minAmt = minAmt
#Self = allows you to access variables, attributes, and methods of a defined class in Python
    
    def getaccNo(self):
        return self.__accNo
    def getaccType(self):
        return self.__accType
    def getbal(self):
        return self.__bal
    def getMinAmt(self):
        return self.__minAmt
    
    def deposit(self,amount):

        if amount >= self.__minAmt:
            self.__bal += amount
            print("Account type: " + self.__accType)
            print("Account number: " + self.__accNo)
            print("Deposited: " + str(amount))
        
        else:
            print("Account type: " + self.__accType)
            print("Account number: " + self.__accNo)
            print("The minimum deposit limit is: " + str(self.__minAmt))
            print("Sorry. the deposit has failed")       

def __str__(self):
        return "Account number: " + str(self.__accNo) + "\nAccount Type: " + self.__accType + "\nThe balance is: " + str(self.__bal)

