# Python email slicer
# Author: Obaid Nadeem
# Python 3.8

email = input("Enter your email: ")

username = email[:email.index("@")]

domain = email[email.index("@")+1:]

print("Name extracted from email is '{}' and the domain extracted is '{}'".format(username,domain))