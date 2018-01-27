persons = ["james", "john", "alice", "bob"]
for name in persons:
    if persons.index(name) % 2 == 0:
        print persons.index(name),name
