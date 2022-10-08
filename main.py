def convertfunction(str1):
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    elif str1[-2:] == "AM":
        return str1[:-2]
    elif str1[:-2] == "PM" and str1[:2] == "12":
        return str1[:-2]
    elif str1[-2:] == "PM" :
        return str(int(str1[:2])+12)+str1[2:-2]
    else:
        print("There is an error in the input")
print (convertfunction("3:32 PM"))