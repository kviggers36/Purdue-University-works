initialBill = int(input("Enter the about of your bill: "))
percentTip = int(input("Enter the tip percentage (in whole numbers): "))
tipCalculation = (initialBill) * (percentTip) / 100
totalBillCalculation = (initialBill) + (tipCalculation)
print(f"A {percentTip}% tip on a bill of ${initialBill} is ${tipCalculation}.")
print(f"Your total bill is ${totalBillCalculation}.")
