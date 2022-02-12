money = float(input("Money: "));
interestRate = float(input("Interest rate: "));
day = int(input("Day: "));

counter = 0;
totalFee = 0;
while (counter < day):
    fee = (float(money / 100) * 0.2) * 2;
    totalFee = totalFee + fee;
    profit = (float(money / 100) * interestRate) - fee;
    print("Profit day", (counter+1), "is", profit);
    money = money + profit;
    
    counter = counter + 1;


print("Total money after", (counter), "days is:", int(money));
print("Total fee paid:", int(totalFee));
