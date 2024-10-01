# From the user
principleamount= (input("enter the principle amount of a CD:"))
yearstomaturity= float(input("enter the years to maturity:"))
if principleamount>=100000 and            yearstomaturity==5: 
  interestrate=0.06
if principleamount>=50000 and yearstomaturity==10: 
  interestrate==0.05
if principleamount>=50000 and yearstomaturity==5: 
  interestrate==0.04
else: 
  interestrate==0.02 
#calculate 

firstyearinterest=principleamount*interestrate
#display
print("Principle amount is:", principleamount, "Interest rate is:", interestrate, "First year interest rate is:", firstyearinterest)