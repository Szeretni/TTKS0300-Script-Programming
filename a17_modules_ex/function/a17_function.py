def printData():
    for key, value in countriesDict.items():
        print key + ":"
        #following 3 lines: Used to manipulate tuple
        i = 0
        tuples0 = ""
        tuples1 = ""
        for key1, value1 in value.items():
            #value(tuple) print
            if (i == 0):
                tuples0 = value1[0]
                tuples1 = value1[1]
                print "\t" + str(key1) + ": " + str(tuples0) + " who is " + str(tuples1) + " years old"
            #value1(float) print
            else:
                print "\t" + str(key1) + ": " +  str(value1) + " million"
            i += 1
