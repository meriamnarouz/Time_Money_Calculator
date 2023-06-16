#Description: This file calculates the breakdown of bills and cents of 
#             a given sum of money. It also calculates the breakdown 
#             of an amount of time given in seconds. 

print("QUESTION 1: \n")
money = input("Please input the total amount of money: ")

#calculations for bills
hundreds = float(money) / 100
hundreds = int(hundreds)

twenties = (float(money) - (hundreds * 100)) / 20
twenties = int(twenties)

tens = (float(money) - ((hundreds * 100) + (twenties * 20))) / 10
tens = int(tens)

fives = (float(money) - (hundreds * 100 + twenties * 20 + tens * 10))/5
fives = int(fives)

ones = float(money) - (hundreds * 100 + twenties * 20 + tens * 10 + fives * 5)
ones = int(ones)

cents = (float(money) - (hundreds * 100 + twenties * 20 + tens * 10 + fives * 5 + ones)) *100
cents = int(cents)

#print output
print("\t" + '{:,}'.format(float(money)) + " is \n\t\t$100 Bills\t" + str(hundreds)
    + "\n\t\t$20  Bills\t" + str(twenties)
    + "\n\t\t$10  Bills\t" + str(tens)
    + "\n\t\t$5   Bills\t" + str(fives)
    + "\n\t\t$1   Bills\t" + str(ones) 
    + "\n\t\tCents Left\t" + str(cents))
    
#For calculating time
print("\nQUESTION 2 \n")
time = input("Please input the time in seconds: ")

#calculations for time
days = int(time)/86400
days = int(days)

hours = (int(time) - (days * 86400))/3600
hours = int(hours)

minutes = (int(time) - (days * 86400 + hours * 3600))/60
minutes = int(minutes)

seconds = int(time) - (days * 86400 + hours * 3600 + minutes * 60)
seconds = int(seconds)

#print output
print("\t" + '{:,}'.format(int(time)) + " seconds are\n\t\t" + str(days) + "\tDays"
    +"\n\t\t" + str(hours) + "\tHours"
    +"\n\t\t" + str(minutes) +"\tMinutes"
    +"\n\t\t" + str(seconds) + "\tSeconds")

