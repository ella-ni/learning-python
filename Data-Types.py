# Learning floats
print(round(6.7))

x=2.4
print(x)

a=round(9.9)
print(a)

# Here comes the strings and some slicing
print("I'm just a little string")

ms_variable = "Judith"
print(ms_variable[0])
print(ms_variable[5])
print(ms_variable[2:6])
print(ms_variable[-1])
print(ms_variable[2:-2])

var = 6
var2 = "6"
print(type(var))
print(type(var2))

infoText = "This is my text"
print(len(infoText))

price = "EUR 109.99"
price_only = price[4:]
print(price_only)


# String Methods - manipulate strings
manipulation = "This is THE text"
print(manipulation.upper())
print(manipulation.lower())
print(manipulation.strip())
test_split = manipulation.split()
print(test_split)
print(manipulation.count("x"))
print(len(manipulation))

pn = "652-58-6548"
pn_p = pn.split("-")
print(pn_p)

my_name = " Saulcerīte Cepurīte "
print(my_name)
name_clean = my_name.strip()
print(name_clean)

# Printing on a new line
my_name = "Saulcerīte \nCepurīte"
print(my_name)


# Checking endswith & startswith
url = "https://www.academia.edu/"
check_url = url.endswith(".edu/")
check_url = url.endswith(".edu/cart")
print(check_url)
check_url_start = url.startswith("https")
print(check_url_start)


# Trying to get rid of some clutter
info = "This%20is%20not%20cluttered%20text."
info_clean = info.replace("%20", " ")
print(info)
print(info_clean)


# String Formatting
# Only on Python2: %s = string, %f = float, %d = integer

my_variable = "I like learning {} programming language".format("Python")
print(my_variable)

my_variable_2 = "{} is {} years old".format("Barbie", 54)
print(my_variable_2)

my_variable_2 = "{name} is {age} years old".format(name ="Barbie", age=54)
print(my_variable_2)

# switching up 
my_variable_2 = "{name} is {age} years old".format(age ="Barbie", name=54)
print(my_variable_2)

# and back again
my_variable_2 = "{0} is {1} years old".format("Barbie", 54)
print(my_variable_2)

# Only on Python 3.7 and above
p_lang = "Java"
variable = f"I do not know if I like {p_lang} so much"
print(variable)

name, age = "Barbie", 54
new_var = f"{name} is {age} years old"
print(new_var)
statement = f"There are {len("Baaaaarbie")} letters in Baaaarbie"
print(statement)