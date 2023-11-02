class SAccount:                                                      #Ari Jacobs - S3958308

    bsbNumber = int(1246)

    def __init__(self, accNo, accType, bal, maxAmt=500.00):
        self.__accNo = accNo
        self.__accType = accType
        self.__bal = bal
        self.__maxAmt = maxAmt
#Self = allows you to access variables, attributes, and methods of a defined class in Python
    
    def getAccNo(self):
        return self.__accNo
    def getAccType(self):
        return self.__accType
    def getBal(self):
        return self.__bal
    def getMinAmt(self):
        return self.__maxAmt
    
    def deposit(self,amount):

        if amount < self.__maxAmt:
            self.__bal += amount
            print("Account type: " + self.__accType)
            print("Account number: " + self.__accNo)
            print("Deposited: " + str(amount))

        else:
            print("Account type: " + self.__accType)
            print("Account number: " + self.__accNo)
            print("The maximum deposit limit is: " + str(self.__maxAmt))
            print("Sorry. the deposit has failed")       

    def __str__(self):
            return "Account number: " + str(self.__accNo) + "\nAccount Type: " + str(self.__accType) + "\nThe balance is: " + str(self.__bal)

