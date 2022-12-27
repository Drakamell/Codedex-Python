'''
10. Currency
Here's the final project of the chapter!

We just got back from a trip to Asia, specifically China, Japan, and South Korea. When we got back we have some leftover cash:

🇨🇳 Chinese yuan
🇯🇵 Japanese yen
🇰🇷 South Korean won
Create a currency.py program that asks the user for the amount they have in yuan, yen, and won and calculates the total in USD.

Make sure to Google the current exchange rates!
'''
# Solution

yuan = (int(input("What do you have left in yuan? ")))
print(yuan)
yen = (int(input("What do you have left in yen? ")))
print(yen)
won = (int(input("What do you have left in won? ")))
print(won)

yuan_to_dollar = yuan * 0.1436 
yen_to_dollar =  yen * 0.0075
won_to_dollar = won * 0.00078

total_dollar = yuan_to_dollar + yen_to_dollar + won_to_dollar

print(total_dollar)