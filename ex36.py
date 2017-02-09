from sys import exit
def winterfell():
    print "Winter is coming?"
    winter = raw_input("yes or no? ")

    if winter == "yes":
        print "You are King of the North!"
        print "Should we invade Kingslanding or go defend the Wall?"
        next = raw_input("Kingslanding or the Wall?")
        if next.lower() == "kingslanding":
            kingslanding()
        else:
            the_wall()
    else:
        dead("You must be a Lannister! DIE!!!")

def kingslanding():
    print "The throne is yours. Do you want it?"
    throne = raw_input("yes or no? ")
    
    if throne == "yes":
        dead("You traitor! DIE!!!")
    else:
        print "You want to defend the Wall then. Let's go!"
        the_wall()

def the_wall():
    print "Good, you are here at the Wall. Should we attack the White Walkers?"
    white_walkers = raw_input("yes or no? ")

    if white_walkers == "yes":
        print "We defeated the White Walkers! You win!!!"
        exit(0)
    else:
        dead("You coward! DIE!!!")

def dead(why):
    print why
    exit(0)

def start():
    print "Do you want to be a Lannister or a Stark?"
    family = raw_input("Lannister or Stark?")

    if family.lower() == "lannister":
        kingslanding()
    else:
        winterfell()

start()
