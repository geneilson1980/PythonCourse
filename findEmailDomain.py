def findEmailDomain(address):
    findSymbol = address.rfind('@')    
    expectedOutput = address[findSymbol+1:]
    return expectedOutput

address = "admin@mailserver2.ru"
result = findEmailDomain(address)
print(result)