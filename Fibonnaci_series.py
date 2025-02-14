while True:
    num1 = (input("Enter first value: "))
    num2 = (input("Enter second value: "))
    sum = num1 + num2
    ctr = int(input("Enter a number of series: "))
    print(num1)
    print(num2)
    print(sum)
    while ctr > 3:
        num1=num2
        num2=sum
        sum =num1+num2
        print(sum)
        ctr=ctr - 1
    answer=input("Do you want to try again? (Yes/No): ")
    if answer == "No":
        print("Thank you for your time")
        break