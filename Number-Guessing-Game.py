import  random
RamdomNumber = random.randrange(1,100)

userNumber =  int(input("Enter the Number : "))

if userNumber > RamdomNumber :
    print("The Number is to High")

    print("The Correct RamdomNumber is : ", RamdomNumber)

elif RamdomNumber > userNumber:

    print("The Number is to Low")

    print("The Correct RamdomNumber is : ", RamdomNumber)

else:

    print("You are to good ")

    print("The Correct RamdomNumber is : ", RamdomNumber)