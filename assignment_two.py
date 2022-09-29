# asking user their name
userName = input("What's your name?:")

# printing and introducing Chatbot
print("Hey there,", userName.capitalize(),"! I'm Chatbot")

# asking where user is from
userLocation = str.lower(input("What country are your from? (ex. United States, China, etc.):"))
'''str.lower chnages all the letters in the input to lower case
.capitalize() makes the first letter of userLocation uppercase'''
#roasting the US
if ("united states" or "us" or "america") in userLocation:
    input("oh...how is that?:")
    print("I used to live there, it was...intresting...anyways,")
else:
    print(userLocation.capitalize(), "is on my bucketlist of places I want to go!")

# asking user what their favorite number is
userNumber = input("What's your favorite number?:")

if float(userNumber) > 0:
    #defining Chatbot's favorite number
    chatNumber = float(userNumber) * 2
    # relating to the users favorite number
    print("Your favorite number is ", userNumber, "?! My favorite number is two times greater than your favorite number",
      chatNumber, "!")
#if the user's favorite number is zero then you print something diffrent:
if float(userNumber) == 0:
    print("Same! Zero's the best")

# ask users dream home
userHome = str.lower(input("What's your dream house?:"))

if ("mansion" or "modern" or "modern house") in userHome:
    print("Are you sure you can you afford one?")
else:
    print("That's fantastic, I'd also love a", userHome, ".")

# asking the cost of the users dream home
userHomeCost = input("How much does your dream house cost?:")
print("Wow, $", userHomeCost, "! I hope you've been saving!")
#aking for their intrest rate
userIntrestRate = input("What's the annual intrest rate?:")

#defining the equation: mohtlyPayments
homeCostNumber = float(userHomeCost)
numberOfMonthlyPayments = 60
intrestRate = float(userIntrestRate)/100/12

monthlyPayments = round((intrestRate * homeCostNumber)/(1-(1+intrestRate)**-numberOfMonthlyPayments),2)

print("Your monthly payemnt will be:", monthlyPayments, "hopefully you can afford that...")