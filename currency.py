#asking for amount of money
userMoney = input("Enter an amount of money in dollars and cents (ex. 162.95):")

# changing user input into numbers the computer can use
decimizedValue = float(userMoney)

# dividing the input to get the amount of 100 dollars it takes
hundredDollars = int(decimizedValue/100)
remainder = round(decimizedValue%100,2) #round(x) rounds the total of the decimized value to ,x (ex. x,2)

# dividing the remainder of the hundred dollars by 50 to get the amount of 50 dollar bills
fiftyDollars = int(remainder/50)
remainderFifty = round(remainder%50,2)

# dividing fifty dollar bills remainder to find how many 25 dollar bills
twentyFiveDollars = int(remainderFifty/25)
remainderTwentyFive = round(remainderFifty%25,2)

#dividing twenty five dollar bills remiander to find how many 10 dollar bills
tenDollars = int(remainderTwentyFive/10)
remainderTen = round(remainderTwentyFive%10,2)

#divinding ten dollar bill remainder to find how many 5 dollar bills
fiveDollars = int(remainderTen/5)
remainderFive = round(remainderTen%5,2)

#dividing five dollar bill remainder to find how many 1 dollar bills
oneDollar = int(remainderFive/1)
remainderOne = round(remainderFive%1,2)

#dividing one dollar bill remiander to find how many quarters
quarterCents = int(remainderOne/0.25)
remainderQuarter = round(remainderOne%0.25,2)

#dividing quarter remainder to find how many dime
dimeCents = int(remainderQuarter/0.10)
remainderDime = round(remainderQuarter%0.10,2)

#dividing dime remainder to find how many nickles
nickleCents = int(remainderDime/0.05)
remainderNickle = round(remainderDime%0.05,2)

# dividing nickle remainder to find how many pennies
pennyCents = int(remainderNickle/0.01)

print(userMoney, "can be made with:",
      hundredDollars, "Hundred dollar(s),",
      fiftyDollars, "Fifty dollar(s),",
      twentyFiveDollars, "Twenty five dollar(s),",
      tenDollars, "Ten dollar(s),",
      fiveDollars, "Five dollar(s),",
      oneDollar, "One dollar(s),",
      quarterCents, "Quarter(s),",
      dimeCents, "Dime(s),",
      nickleCents, "Nickle(s), and ",
      pennyCents, "Pennies")