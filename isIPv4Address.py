# An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

# Given a string, find out if it satisfies the IPv4 address naming rules.

# def isIPv4Address(inputString):
#     isIPv4 = False
#     dotsList = []
#     findDots = inputString.find('.')
#     if findDots == -1:
#         return isIPv4
#     elif inputString.count('.') != 3:
#         return isIPv4
#     else:
#         for dot, char in enumerate(inputString):
#             if '.' in char:
#                 dotsList.append(dot)
#         setNumbers1 = inputString[0:dotsList[0]].isdigit()
#         setNumbers2 = inputString[dotsList[0]+1:dotsList[1]].isdigit()
#         setNumbers3 = inputString[dotsList[1]+1:dotsList[2]].isdigit()
#         setNumbers4 = inputString[dotsList[2]+1:].isdigit()
#         if inputString[0:dotsList[0]] == '00' or inputString[0:dotsList[0]] == '000' or inputString[dotsList[0]+1:dotsList[1]] == '00' or inputString[dotsList[0]+1:dotsList[1]] == '000' or inputString[dotsList[1]+1:dotsList[2]] == '00' or inputString[dotsList[1]+1:dotsList[2]] == '000' or inputString[dotsList[2]+1:] == '00' or inputString[dotsList[2]+1:] == '000':
#             return isIPv4
#         if setNumbers1 and setNumbers2 and setNumbers3 and setNumbers4:
#             setNumbers1 = int(inputString[0:dotsList[0]])
#             setNumbers2 = int(inputString[dotsList[0]+1:dotsList[1]])
#             setNumbers3 = int(inputString[dotsList[1]+1:dotsList[2]])
#             setNumbers4 = int(inputString[dotsList[2]+1:])
#             if setNumbers1 < 100 and len(inputString[0:dotsList[0]]) > 1:
#                 temp1 = inputString[0:dotsList[0]]
#                 temp2 = temp1[0]
#                 if temp2 == '0':
#                     return isIPv4
#             if setNumbers2 < 100 and len(inputString[dotsList[0]+1:dotsList[1]]):
#                 temp1 = inputString[dotsList[0]+1:dotsList[1]]
#                 temp2 = temp1[0]
#                 if temp2 == '0':
#                     return isIPv4      
#             if setNumbers3 < 100 and len(inputString[dotsList[1]+1:dotsList[2]]):
#                 temp1 = inputString[dotsList[1]+1:dotsList[2]]
#                 temp2 = temp1[0]
#                 if temp2 == '0':
#                     return isIPv4
#             if setNumbers2 < 100 and len(inputString[dotsList[2]+1:]):
#                 temp1 = inputString[dotsList[2]+1:]
#                 temp2 = temp1[0]
#                 if temp2 == '0':
#                     return isIPv4
#         else:
#             return isIPv4
#         if (setNumbers1 < 0 or setNumbers1 > 255) or (setNumbers2 < 0 or setNumbers2 > 255) or (setNumbers3 < 0 or setNumbers3 > 255) or (setNumbers4 < 0 or setNumbers4 > 255) :
#             return isIPv4
#         else:
#             isIPv4 = True
#             return isIPv4

def isIPv4Address(inputString):
    ipInput = inputString.rstrip().split('.')
    if len(ipInput) != 4:
        return False
    for i in ipInput:
        if not(i.isdigit()) or i == '' or int(i) < 0 or int(i) > 255:
            return False
        if checkValidSet(i):
            return False
    return True

def checkValidSet(value):
    if len(value) == 1 and value[0] == '0':
        return False
    if value[0] == '0' and int(value[1]) >= 0:
        return True
    return False


inputString = "1.23.256.."
result = isIPv4Address(inputString)
print(result)

# I have to solve the error when I have a value below 10
# I have to solve the error when I have a value below 100