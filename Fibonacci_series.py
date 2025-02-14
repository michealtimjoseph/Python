# Improve fibonacci series
while True:
    num1 = (input("\nEnter first value: "))
    num2 = (input("Enter second value: "))
    sum = int(num1) + int(num2)
    ctr = int(input("Enter a number of series: "))
    print(num1)
    print(num2)
    print(sum)
    while ctr > 3:
        num1=num2
        num2=sum
        sum= int(num1) + int(num2)
        print(sum)
        ctr=ctr - 1
    answer=input("Do you want to try again? (Yes/No): ")
    if answer == "no":
        print("Thank you for your time")
        break
