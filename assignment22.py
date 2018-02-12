'''Refactoring
This function adds an element to a list inside a dict of lists.
Rewrite it to use a try-except statement which handles a possible KeyError if the list with the
name provided doesn't exist in the dictionary yet, instead of checking beforehand whether it does.
Include else and finally clauses in your try-except block:
'''

thedict = {} # You can use existing dict as well
# function takes a dict, a list name and the element
def add_to_list_in_dict(thedict, listname, element):
    #define l, it is also used in except
    l = thedict
    try:
        listname in thedict
        l = thedict[listname]
    except KeyError: #key doesn't exist
        print "KeyError occured and handled."
        print("Created %s." % listname)
        print("%s already has %d elements." % (listname, len(l)))
        thedict[listname] = []
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))

print thedict #dict is empty
add_to_list_in_dict(thedict, "key", "value")
add_to_list_in_dict(thedict, "key1", "value1")
print thedict #dict has KeyValuePairs

'''prints
{}
KeyError occured and handled.
Created key.
key already has 0 elements.
Added value to key.
KeyError occured and handled.
Created key1.
key1 already has 1 elements.
Added value1 to key1.
{'key1': ['value1'], 'key': ['value']}
>>> 
'''
'''initial code
thedict = [] # You can use existing dict as well
# function takes a dict, a list name and the element
def add_to_list_in_dict(thedict, listname, element):
    if listname in thedict:
        l = thedict[listname]
        print("%s already has %d elements." % (listname, len(l)))
    else:
        thedict[listname] = []
        print("Created %s." % listname)
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))
thedict[listname].append(element)
print("Added %s to %s." % (element, listname))
'''
