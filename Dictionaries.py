# dictionary as a key & value pair, each pair separated by comma
# not sequenced, so indexing is not possible
# mutable (you can add and remove elements)

{
    "first_name": "Žube",
    "last_name": "Žubīte",
    "id_number": 63548
}

exam_score = {"Emily": 86, "Marc":52, "Kate": 25}

# getting an item from a dictionary
element = exam_score.get("Kate")
print(element)

element_1 = exam_score["Marc"]
print(element_1)

# returning default value if the key doesn't exist
element_billy = exam_score.get("Billy")
print(element_billy)


# adding an item
exam_score["Ninja"] = 100
print(exam_score)

# another way to add - built in update bn               
exam_score.update({"Lara" : 72})
print("Another way to add an item")
print(exam_score)

# dictionaries also have methods (getting list of the keys and the values)
capitals = {"Germany" : "Berlin", "Canada" : "Ottawa", "Estonia" : "Tallin", "England" : "London"}
print(capitals.values())
print(type(capitals.values()))
print(capitals.keys())


canada_capital = capitals["Canada"]
print(canada_capital)

# getting non existent key
# japan_capital = capitals["Japan"] - will get keyerror
japan_capital = capitals.get("Japan")
print(japan_capital)

# returning default value - cooler than key error
japan_capital2 = capitals.get("Japan", "Capital of this country is not added!")
print(japan_capital2)

# just another longer dictionary example
student_card = {
    "name" : "Nadia Tomson",
    "age" : 22,
    "phone" : 3648256974,
    "program" : "Medicine",
    "courses" : ["Anatomy", "Microbiology", "Internal medicine", "Pharmacology", "Physiology"]
}

student_name = student_card["name"]
student_age = student_card["age"]
student_courses = student_card["courses"]

print(type(student_courses))
user_courses_count = len(student_courses)
print(f"Student has to attend {user_courses_count} courses")

