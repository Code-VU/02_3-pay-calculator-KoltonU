def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    hrs = float(input("Enter Hours:"))
    rate = float(input("Enter Hourly Rate:"))
    gross_pay = (hrs * rate)
    print('$',gross_pay)



    # end assignment


## If you want to test locally before you try to sync
## Open your terminal and run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
