countryCodesList = ["fi","se","no"]
codeMapDict =  {
  countryCodesList[0]: "Finland",
  countryCodesList[1]: "Sweden",
  countryCodesList[2]: "Norway"
}
countriesDict =  {
  codeMapDict[countryCodesList[0]]:{"head honcho":("Juha Sipila",54),"population":5.439},
  codeMapDict[countryCodesList[1]]:{"head honcho":("Stefan Lofven",58),"population":9.593},
  codeMapDict[countryCodesList[2]]:{"head honcho":("Erna Solberg",54),"population":5.084}
}
for key, value in countriesDict.iteritems():
    print key + ":\n\t" + str(value.iteritems())
'''
for key, value in countriesDict.iteritems():
    print key + ":"
    for key1, value1 in value.iteritems():
        print "\t" + key1 + ": " + str(value1)
   '''     
'''
for i in range(0,3):
    print codeMapDict[countryCodesList[i]] + "\n\t" + str(countriesDict[codeMapDict[countryCodesList[i]]])
'''
'''
for key in countriesDict:
    print countriesDict[key]
'''
'''
print countryCodesList
print codeMapDict
print countriesDict
'''

