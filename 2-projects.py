print("Welcome to the rollercoaster!")
bill = 0
height = int(input("What is your height in cm? "))

if height >= 120 and height <= 200:
    age = int(input("How old are you? "))
    wants_photo = input("Do you want a photo taken? Y or N.")
    if age < 12:
        bill = 5
        print("Child tickets are 5$ ")
    elif age <= 18:
        bill = 7
        print("Youth tickets are 7$")
    elif age >= 45 and age <= 55:
        bill= 0 
        print("Everything is going to be ok. Have a free ride on us! ")
    else:
        bill = 12
        print("Adult tickets are 12$")

    if wants_photo == "Y":
        bill += 3

    print(f"Your finall bill is ${bill}")

else:
    print("You can not ride the rollerocaster")