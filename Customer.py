class Customer:                                           #Ari Jacobs - S3958308
     
    bsbNo = 1246
    def __init__(self, custNo, custNm, age, city, accObj):
        self.__custNo = custNo
        self.__custNm = custNm
        self.__age = age
        self.__city = city
        self.__accObj = accObj
#Self = allows you to access variables, attributes, and methods of a defined class in Python

    def getcustNo(self):
        return self.__custNo
    
    def getcustNm(self):
        return self.__custNm
    
    def getage(self):
        return self.__age
    
    def getcity(self):
        return self.__city
    
    def getaccObj(self):
        return self.__accObj
    
def __str__(self):
        return "Customer number: " + str(self.__custNo) + "\nCustomer Name: " + self.__custNm + "\nAge: " + str(self.__age) + "\nCity: " + self.__city
    