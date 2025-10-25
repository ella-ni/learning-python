# Decision is based on condition being TRUE or FLASE
# Each statement must end with semicolon :
# else is optional

# if <something is true>:
#     <do this>
# else:
#     <do something else>

a = 20
b = 6
c = 30
d = 10

if a < b:
    print("'a' is less than 'b'")
elif (a > b) and (a < c):
    print("'a' is greater than 'b'")
else:
    print("N/A")


# checking multiple condition use "elif"
# keep checking until TRUE is found or ELSE is reached
# if <something is true>:
#     <do this>
# elif <something else is true>:
#     <do this>
# else:
#     <do this if none of the above>


shows = ["Game of Thrones", "The Office", "The Big Bang Theory", "Friends"]
movies = ["The Secret Life of Pets", "Murder Mystery", "Pride & Prejudice", "We Bought a Zoo"]

my_choice = "Friends"

# if my_choice in shows:
#     print("Your choice is a show")
# elif my_choice in movies:
#     print("Your choice is a movie")
# else:
#     print("Your choice is unknown")

if (my_choice in shows) or (my_choice in movies):
    print("Your choice is valid")
else:
    print("Unknown")