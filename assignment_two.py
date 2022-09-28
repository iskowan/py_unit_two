# asking user their name
userName = input("What is your name?:")

# printing and introducing Chatbot
print("G'day", userName,"! I'm Chatbot")

# asking where user is from
userLocation = str.lower(input("Where country are your from?:"))
    #str.lower chnages all the letters in the input to lower case

#depending on the input, the bot will reply
if ("us" or "america") in userLocation:
    print("oh...")
else:
    print(userLocation, "is on my bucketlist of places I want to go!")

# asking user what their favorite number is
userNumber = input("What's your favorite number?:")

#defining Chatbot's favorite number
chatNumber = float(userNumber) * 2
# relating to the users favorite number
print("Your favorite number is ", userNumber, "?! My favorite number is two times greater than your favorite number", chatNumber)

# ask users dream home
userHome = input("What's your dream house?:")
print("Thats fantastic, I'd also love a(n)", userHome, ".")
# asking the cost of the users dream home
userHomeCost = input("How much does your dream house cost?:")
print("Wow, $", userHomeCost, "! Is that in your budget!?")
#aking for their intrest rate
userIntrestRate = input("What is the annual intrest rate?:")

numberOfMonthlyPayments = 60
#defining the equation: mohtlyPayments
P = float(userHomeCost)
n = numberOfMonthlyPayments
r = float(userIntrestRate)/100/12

monthlyPayments = round((r * P)/(1-(1+r)**-n),2)

print("Your monthly payemnt will be:", monthlyPayments)