#Version 2018-02-19
'''
Write a function speeding_ticket that is given the speed of a car and the speed limit. The function
should return a tuple that contains information about the amount of the fine and whether or not the
driver loses his license. If the car’s speed exceeds the speed limit by 5 km/h the driver receives
a fine of 100€ and if the car’s speed exceeds the speed limit by 20km/h he gets a fine of 500€ and
loses his license.

The returned tuple should contain the amount of the fine as the first value and a boolean informing
whether or not the driver lost his license (True loses license, False does not).

print speeding_ticket(50, 50) # No fine. prints: (0, False)
print speeding_ticket(60, 50) # 100€ fine, doesn't lose license. Prints: (100, False)
print speeding_ticket(100, 50) # 500€ fine, loses license. Prints: (500, True)
'''

def speeding_ticket(car,limit):
    fine = 0
    lose_licence = False
    if (car > limit + 5):
        fine = 100
    if (car > limit + 20):
        fine = 500
        lose_licence = True
    outcome = (fine,lose_licence)
    print(outcome)

#calls
speeding_ticket(50, 50)
speeding_ticket(60, 50)
speeding_ticket(100, 50)

#prints
'''
(0, False)
(100, False)
(500, True)
'''
