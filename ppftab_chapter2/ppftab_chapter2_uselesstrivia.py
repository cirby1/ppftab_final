#This program takes three pieces of information from the user.

name = input("Hi. What's your name? ")
age = int(input("How old are you? "))
weight = input("Okay. Last question. How many pounds do you weigh? ")
print()

print("If a poet ee cummings were to email you, he'd address you as " + name)
print("But if ee were mad, he'd call you as " + name.upper())
print()

print("If a small child were trying to get your attention")
print("your name would become:")
print(name.title()*5)
print()

print(age)
seconds = age * 31,536,000
print("You're over " + str(seconds) + " seconds old.")
