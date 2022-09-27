# asking user their name
userName = input("What is your name?:")

# printing and introducing Chatbot
print("Hi", userName,"! I'm Chatbot")

# asking where user is from
userLocation = input("Where are your from?:")

# complementing users location
print(userLocation, "is actually on my bucketlist of places I want to go!")

# asking user what their favorite number is
userNumber = input("What's your favorite number?:")

#defining Chatbot's favorite number
chatNumber = float(userNumber) * 2
# relating to the users favorite number
print("Your favorite numberis ", userNumber, "?! My favorite number is two times your favorite number", chatNumber)

# ask users dream home
userHome = input("What's your dream home?:")
print("I also want a", userHome, ".")
# asking the cost of the users dream home
userHomeCost = input("How much does your dream home cost?:")
print("Wow, $", userHomeCost, "! Is that in your budget?")
#aking for their intrest rate
userIntrestRate = input("What is the intrest rate?:")

#defining the equation: mohtlyPayments
P = float(userHomeCost)
n = 60
r = float(userIntrestRate)/100/12

monthlyPayments = round((r * P)/(1-(1+r)**-n),2)

print("Your monthly payemnt will be:", monthlyPayments)