def depositProfit(deposit, rate, threshold):
    year = 1
    calc = ((deposit / 100) * rate) + deposit
    while True:
        if calc < threshold:
            year += 1
            newBaseValue = calc
            calc = ((newBaseValue / 100) * rate) + newBaseValue
        else:
            return year

deposit = 50
rate = 25
threshold = 100
result = depositProfit(deposit, rate, threshold)
print(result)