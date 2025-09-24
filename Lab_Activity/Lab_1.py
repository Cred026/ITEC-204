def prob_1():
    total_paid_employee = 0

    while(True):
        numOfWorkers = int(input("How many workers are there: "))
        if (numOfWorkers <=0 ): 
            print("Please enter a correct amount ")
            continue

        for i in range(2):
            name = input("Empoyee Name: ")
            hourlyRate = int(input("Hourly Rate: "))
            HoursWorked = int(input("Number of Hours wokred: "))
            Overtime = int(input("Overtime hours: "))
            LateHours = int(input("Late hours: "))

            overtimePayment = (hourlyRate / 8) * Overtime
            deductionPayment = (LateHours * hourlyRate)
            totalSalary = (hourlyRate * HoursWorked) + overtimePayment - deductionPayment

            total_paid_employee += totalSalary
            
            print("-------------------------------------------------")
            print("")
            print("")

            print(f"Payroll Summary Employye {i+1} : ")
            print(f"Name of employee: {name}")
            print(f"Hourly Rate: {hourlyRate}")
            print(f"Hours Worked: {HoursWorked}")
            print(f"Overtime: {overtimePayment}")
            print(f"Latehours: {LateHours}")

            print("\nCalculatins\n")

            print(f"Overtime Payment: {overtimePayment}")
            print(f"Deduction for late: {deductionPayment}")
            print(f"Total salary: {totalSalary}")
            print("")
            print("")
            print("-------------------------------------------------")

            if(i >= numOfWorkers):
                break
            else:
                continue

        print(f"Total paid {total_paid_employee}")
        break

def prob_2():
    pricipalAmount = float(input("Principal Amount: "))
    interest = float(input("Enter Interest: "))
    loanDurationInMonths = int(input("Loan Duration: "))
    tempamount = pricipalAmount

    for i in range(loanDurationInMonths):

        monthly_principal_payment = pricipalAmount / loanDurationInMonths
        remaining_balance = tempamount - monthly_principal_payment
        tempamount -= monthly_principal_payment
        monthly_interest =  (remaining_balance + monthly_principal_payment) * (interest/100)
        monthly_due = monthly_principal_payment + monthly_interest

        print("\n---------------------------------------------------\n")

        print(f"Month {i+1}")
        print(f"Monthly Amount: {monthly_principal_payment}")
        print(f"Interest: {interest}%")
        print(f"Monthly Interest: {monthly_interest}")
        print(f"Monthly Due: {monthly_due}")
        print(f"Remaining Balance: {remaining_balance + monthly_principal_payment}")

        print("\n---------------------------------------------------\n")

