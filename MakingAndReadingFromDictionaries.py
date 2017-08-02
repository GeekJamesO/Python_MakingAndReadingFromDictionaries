# Assignment: Making and Reading from Dictionaries
# Create a dictionary containing some information about yourself.
# The keys should include name, age, country of birth, favorite language.
#
# Write a function that will print something like the following as it executes:
#
#     My name is Anna
#     My age is 101
#     My country of birth is The United States
#     My favorite language is Python
#
# There are two steps to this process, building a dictionary and then gathering
# all the data from it. Write a function that can take in and print out any
# dictionary keys and values.
#
# Note: The majority of data we will manipulate as web developers will be
# hashed in a dictionary using key-value pairs. Repeat this assignment a few
# times to really get the hang of unpacking dictionaries, as it's a very common
# requirement of any web application.

#create a dictionary about me
myDictonary = {
    "age" : "18",
    "birthCountry" : "United States of America",
    "favLanguage" : "Americian Sign Language",
    "name" : "James C. O'Rourke"
}

def PrintPersonData(inDict) :
    print inDict
    print ("    My name is {0}.".format( inDict['name']) )
    print ("    My age is {0}.".format (  inDict['age']) )
    print ("    My country of birth is {0}.".format (  inDict['birthCountry']) )
    print ("    My favorite language is {0}.".format( inDict['favLanguage']) )

PrintPersonData(myDictonary)
