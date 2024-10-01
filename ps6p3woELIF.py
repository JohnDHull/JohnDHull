#Haniya Fatima Week 6 ASN 6 Problem 3

#input phase
principle = float(input("Enter the principle amount: "))
yrMaturity = int(input("Enter the year of maturity: "))

#process phase
if principle > 100000 and yrMaturity == 5:
  interestRate = 0.06
else:
  if principle >= 50000 and principle <= 100000 and yrMaturity == 10:
    interestRate = 0.05
  else:
    if principle >= 50000 and principle <= 100000 and yrMaturity == 5:
      interestRate = 0.04
    else:
      interestRate = 0.02

interest = principle * interestRate

#output phase
print("Principle: $", principle)
print("Interest Rate: ", interestRate)
print("Interest Amount for first year: $", interest)