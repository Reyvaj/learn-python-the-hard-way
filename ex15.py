# imports the argv module.
from sys import argv
# sets de variables to script and filename.
script, filename = argv
# opens the file given in filename and puts its content into txt variable.
txt = open(filename)
# prints a statement with the name of the filename.
print "Here's your file %r:" % filename
# prints the content of txt into the screen.
print txt.read()
# prints a statement.
print "Type the filename again:"
# asks the user for input and stores it in the file_agian variable.
file_again = raw_input("> ")
# opens the file in file_again and stores its content in txt_again.
txt_again = open(file_again)
# prints the content of txt_again into the screen.
print txt_again.read()
