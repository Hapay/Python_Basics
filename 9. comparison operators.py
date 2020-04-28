temperature = 20
if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's neither cold nor hot")

"""Exercise
If name is less than 3 chars long 
    name must be at least 3 characters long
otherwise if it's more than 50 chars long
    name can be at maximum of 50 chars
otherwise
    you are good. name is fine
"""

name = "Patryk"
if len(name) < 3:
    print("Name is too short!")
elif len(name) > 50:
    print("Name is too long!")
else:
    print("Your name is fine")
