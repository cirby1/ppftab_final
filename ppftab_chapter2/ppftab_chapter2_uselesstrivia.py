#This program takes three pieces of information from the user.

name = input("Hi. What's your name? ")
age = int(input("How old are you? "))
weight = float(input("Okay. Last question. How many pounds do you weigh? "))
print()

print("If a poet ee cummings were to email you, he'd address you as " + name)
print("But if ee were mad, he'd call you as " + name.upper())
print()

print("If a small child were trying to get your attention")
print("your name would become:")
print(name.title()*5)
print()

#print(age)
seconds = 0
seconds = age * (31536000)
print("You're over " + str(seconds) + " seconds old.")
print()

#Formula for calculating weight on the moon is: (Weight on Earth/Gravity on Earth) x Gravity on Moon. (165 Ibs/9.8 Earth Gravity) * 1.6 Moon Gravity.
#print(weight)
moonweight = (float(weight) / 9.8) * 1.6
sunweight = (float(weight) / 9.8) * 27.9
print("Did you know on the moon you would weigh only " + str(moonweight) + " pounds?")
print("On the sun, you'd weigh " + str(sunweight) + " <but, ah... not for long>.")
#print(moonweight)


