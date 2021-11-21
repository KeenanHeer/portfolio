

def main(askForNumber):
    if(askForNumber<=5):
        if(askForNumber == 2 or askForNumber==3 or askForNumber ==5):
            print('This is a prime')
        else:
            print('This is not a prime')
    for num in range(2,askForNumber//2):
        print(num)
        if askForNumber%num == 0:
            print("it is not prime")
            break
        else:
            if(num == (askForNumber//2)-1):
                print("it is prime")
               

userNumberInput = int(input("Ask me any number and I will tell you if it is prime "))

main(userNumberInput)
