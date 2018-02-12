# -*- coding: cp1252 -*-
'''Refactoring
This function adds an element to a list inside a dict of lists.
Rewrite it to use a try-except statement which handles a possible KeyError if the list with the
name provided doesn’t exist in the dictionary yet, instead of checking beforehand whether it does.
Include else and finally clauses in your try-except block:
'''

thedict = {"existing":"elem"} # You can use existing dict as well
# function takes a dict, a list name and the element
def add_to_list_in_dict(thedict, listname, element):
    try:
        listname in thedict
        l = thedict[listname]
        print("%s already has %d elements." % (listname, len(l)))
    except KeyError:
        print "KeyError occured and handled"
        thedict[listname] = []
        print("Created %s." % listname)
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))

print thedict #dict is empty
add_to_list_in_dict(thedict, "key", "value")
print thedict #dict has one KeyValuePair

'''prints
{}
KeyError occured and handled
key already has 0 elements.
Created key.
Added value to key.
{'key': ['value']}
>>> 
'''
