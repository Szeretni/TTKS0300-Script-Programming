#Version 2018-02-12
'''
This function adds an element to a list inside a dict of lists.
Rewrite it to use a try-except statement which handles a possible KeyError if the list with the
name provided doesn't exist in the dictionary yet, instead of checking beforehand whether it does.
Include else and finally clauses in your try-except block:
'''

thedict = {} #defining new dict
def add_to_list_in_dict(thedict, listname, element):
    try: #adding elements to existing list
        thedict[listname].append(element) #adding element
    except KeyError: #key ie. list doesn't exist
        thedict[listname] = [] #defining list
        print("\nList doesn't exist. Created %s list." % listname)
        thedict[listname].append(element) #adding element
        print("Added %s to %s." % (element, listname))
    else:
        print("\nAdded %s to existing %s." % (element, listname))
        print("%s has now %d elements." % (listname, len(thedict[listname])))
    finally:
        print("Complete dict below:\n%s" % thedict)

add_to_list_in_dict(thedict, "animals", "dog")
add_to_list_in_dict(thedict, "components", "cpu")
add_to_list_in_dict(thedict, "components", "power")

#prints
'''
List doesn't exist. Created animals list.
Added dog to animals.
Complete dict below:
{'animals': ['dog']}

List doesn't exist. Created components list.
Added cpu to components.
Complete dict below:
{'animals': ['dog'], 'components': ['cpu']}

Added power to existing components.
components has now 2 elements.
Complete dict below:
{'animals': ['dog'], 'components': ['cpu', 'power']}
'''
#initial code
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
