money = float(input("Money: "));
interestRate = float(input("Interest rate: "));
day = int(input("Day: "));

counter = 0;

while (counter < day):
    profit = float(money / 100) * interestRate;
    print("Profit day ", (counter+1), " is", profit);
    money = money + profit;
    
    counter = counter + 1;


print("Total money ", (counter), " is ", money);
