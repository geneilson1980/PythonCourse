# Call two arms equally strong if the heaviest weights they each are able to lift are equal.

# Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

# Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    yourStrongestArm = max(yourLeft, yourRight)
    friendStrongestArm = max(friendsLeft, friendsRight)
    yourCapabilities = yourLeft + yourRight
    friendCapabilities = friendsLeft + friendsRight
    areEquallyStrong = True
    if (yourStrongestArm == friendStrongestArm) and (yourCapabilities != friendCapabilities):
        areEquallyStrong = False
        return areEquallyStrong
    elif (yourStrongestArm != friendStrongestArm) and (yourCapabilities == friendCapabilities):
        areEquallyStrong = False
        return areEquallyStrong
    elif (yourCapabilities != friendCapabilities):
        areEquallyStrong = False
        return areEquallyStrong
    return areEquallyStrong

yourLeft = 5
yourRight = 5
friendsLeft = 10
friendsRight = 10

result = areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight)
print(result)



    # yourStrongestArm = 0
    # friendStrongestArm = 0
    # if yourLeft > yourRight:
    #     yourStrongestArm = yourLeft
    # else:
    #     yourStrongestArm = yourRight
    # if friendsLeft > friendsRight:
    #     friendStrongestArm = friendsLeft
    # else:
    #     friendStrongestArm = friendsRight
    # yourCapabilities = yourLeft + yourRight
    # friendCapabilities = friendsLeft + friendsRight
    # areEquallyStrong = True
    # if (yourStrongestArm == friendStrongestArm) and (yourCapabilities != friendCapabilities):
    #     areEquallyStrong = False
    #     return areEquallyStrong
    # elif (yourStrongestArm != friendStrongestArm) and (yourCapabilities == friendCapabilities):
    #     areEquallyStrong = False
    #     return areEquallyStrong
    # elif (yourCapabilities != friendCapabilities):
    #     areEquallyStrong = False
    #     return areEquallyStrong
    # return areEquallyStrong