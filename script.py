choice = "yes"
#The program greets user and describes what's the purpose of the program.
print("Hi, this programm will convert kilometers into miles.")
#The program asks user to enter number of kilometers.
km = input("Enter the number of kilometers you want to convert ")
km = float(km.replace(",", ".")) #replace comma with dot, if user entered a comma
#print(km)
mi = float(km)*0.621371
#print(mi)
mi = round(mi, 2)
#User enters the amount of kilometers.
#The program converts these kilometers into miles and prints them.
print(str(km) + " kilometers are ~ " + str(mi) + " miles".format(km, mi))
#The program asks user if s/he'd want to do another conversion.
while choice != "n":
    choice = input("Do another conversion? (y/n) ")
#If yes, repeat the above process (except the greeting).
    if choice == "y":
        km = input("Enter the number of kilometers you want to convert ")
        mi = float(km) * 0.621371
        mi = round(mi, 2)
        print(str(km) + " kilometers are ~ " + str(mi) + " miles")
    #If not, the program says goodbye and stops.
    elif choice == "n":
        print("Thank you and goodbye!")
        break
    else:
        print("Type 'y' or 'n'")