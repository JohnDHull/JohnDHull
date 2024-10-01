Principle = float(input("Enter principle amount: "))
Maturity = float(input("Enter year to maturity: "))
if Principle > 100000 and Maturity == 5:
  IR = 0.06
elif Principle >= 50000 and Principle <= 100000 and Maturity == 10:
  IR = 0.05
elif Principle >= 50000 and Principlee <= 100000 and Maturity == 5:
  IR = 0.04
else:
  IR = 0.02
Firstyear = Principle * IR
print("Principle: ", Principle, "\nInterest rate: ", IR, "\nInterest amount for first year: ", Firstyear)