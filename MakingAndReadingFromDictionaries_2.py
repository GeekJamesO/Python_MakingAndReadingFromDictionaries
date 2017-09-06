print "Assignment: Making and Reading from Dictionaries"
print "Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language."
print ""
print "Write a function that will print something like the following as it executes:"
print ""
print ""
print "There are two steps to this process, building a dictionary and then gathering all the data from it. "
print "Write a function that can take in and print out any dictionary keys and values."
print ""
print "Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. "
print "Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement of any web application."

def printAboutMe(dic):
    print "   My name is {}".format(dic['name'])
    print "   My age is {}".format(dic['age'])
    print "   My country of birth is {}".format(dic['birthCountry'])
    print "   My favorite language is {}".format(dic['favLanguage'])

aboutMe = { "age" : "30ish", "birthCountry" : "United States of America", "favLanguage" : "Americian Sign Language","name" : "James C. O'Rourke" }

printAboutMe(aboutMe)
