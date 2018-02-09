countryCodesList = ["fi","se","no"]
codeMapDict =  {
  countryCodesList[0]: "Finland",
  countryCodesList[1]: "Sweden",
  countryCodesList[2]: "Norway"
}
countriesDict =  {
  #key----------------------------<#value------------------------------------------------<
                                    #key1-------< #value1-----------<#key1-------<#value1<
  codeMapDict[countryCodesList[0]]:{"head honcho":("Juha Sipila",54),"population":5.439},
  codeMapDict[countryCodesList[1]]:{"head honcho":("Stefan Lofven",58),"population":9.593},
  codeMapDict[countryCodesList[2]]:{"head honcho":("Erna Solberg",54),"population":5.084}
}
for key, value in countriesDict.items():
    print key + ":"
    #i index used to differentiate value1 tuples and float
    i = 0
    for key1, value1 in value.items():
        #value1(tuple) print
        if (i == 0):
            tuples0 = value1[0]

            tuples1 = value1[1]
            print "\t" + str(key1) + ": " + str(tuples0) + " who is " + str(tuples1) + " years old"
        #value1(float) print
        else:
            print "\t" + str(key1) + ": " +  str(value1) + " million"
        i += 1
        
#prints
'''
Sweden:
	head honcho: Stefan Lofven who is 58 years old
	population: 9.593 million
Finland:
	head honcho: Juha Sipila who is 54 years old
	population: 5.439 million
Norway:
	head honcho: Erna Solberg who is 54 years old
	population: 5.084 million
'''
