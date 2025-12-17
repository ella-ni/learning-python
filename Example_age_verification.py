
movie_name = "Sharp Roses"
age_limit = 17

print(f"Welcome to {movie_name} movie!")


user_input = input("Enter your age: ")
print(f"User input is: {user_input}")

if int(user_input) >= age_limit:
    print("Welcome...welcome")
else:
    print("Sorry there's this age limit thing!")