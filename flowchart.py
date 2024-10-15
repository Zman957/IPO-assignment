movie = 8

Harry = 7

Judy = 12



if Judy < movie:
    print ("Sorry you cannot watch this movie")
elif Judy >= movie:
    print ("judy can watch the movie")

if Harry < movie:
    print("Sorry you cannot watch this movie Harry, not enough money")
    print( "You would still owe", Harry - movie, "dollar")

print("If you both cannot pay for a ticket we recommend the Arcade")

arcade = 6

if Judy < arcade:
    print ("Sorry you cannot watch this movie")
elif Judy >= arcade:
    print ("Judy can play at the arcade")

if Harry < arcade:
    print ("Sorry you cannot watch this movie")
elif Harry >= arcade:
    print ("Harry can play at the arcade")


