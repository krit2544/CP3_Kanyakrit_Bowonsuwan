usernameInput = input("UserName : ")
passwordInput = input("Password : ")

if usernameInput == "Boss" and passwordInput == "1234":
    print("Done, Welcome !!")

    print("Welcome to AYE Shop !!")
    print("----------------------")
    print("What do you want ?")
    print("1.Cola 20 Bath")
    print("2.Water 10 Bath")
    print("3.Snack 5 Bath")
    print("4.Noodle 15 Bath")
    print("5.Exit")
    userSelected1 = int(input(">>"))
    if userSelected1 == 1:
        print("Cola 20 Bath")
        qualityCola = int(input("How many do you want : "))
        quality1 = qualityCola*20
        print("Total price of Cola : ",quality1,"Bath")
    elif userSelected1 == 2:
        print("Water 10 Bath")
        qualityWater = int(input("How many do you want :"))
        quality2 = qualityWater*10
        print("Total price of Water :",quality2,"Bath")
    elif userSelected1 == 3:
        print("Snack 5 Bath")
        qualitySnack = int(input("How many do you want :"))
        quality3 = qualitySnack * 5
        print("Total price of Snack :", quality3, "Bath")
    elif userSelected1 == 4:
        print("Noodle 15 Bath")
        qualityNoodle = int(input("How many do you want :"))
        quality4 = qualityNoodle * 15
        print("Total price of Noodle :", quality4, "Bath")
    elif userSelected1 == 5:
        print("Bye Bye")
    else:
        print("Error")
else:
    print("Wrong Username or Password , Try again.")