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

print countryCodesList
print codeMapDict
print countriesDict

#prints
'''
['fi', 'se', 'no']
{'fi': 'Finland', 'se': 'Sweden', 'no': 'Norway'}
{'Sweden': {'head honcho': ('Stefan Lofven', 58), 'population': 9.593}, 'Finland': {'head honcho': ('Juha Sipila', 54), 'population': 5.439}, 'Norway': {'head honcho': ('Erna Solberg', 54), 'population': 5.084}}
'''
