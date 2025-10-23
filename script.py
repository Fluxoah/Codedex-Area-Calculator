import os
import math
os.system("cls")

while True:
    print("   ==================")
    print("   Area Calculator 📐")
    print("   ==================")
    
    print("""\n    1. Triangle
    2. Rectangle
    3. Square
    4. Circle
    5. Quit\n""")
    
    choice = int(input("Which shape >> "))
    
    if choice == 1 or choice == "triangle":
        Height = int(input("\nHeight >> "))
        Base = int(input("Base >>"))
        area = (Height * Base) / 2
    elif choice == 2 or choice == "rectangle":
        Length = int(input("\nLength >> "))
        Width = int(input("Width >> "))
        area = Length * Width
    elif choice == 3 or choice == "square":
        Side = int(input("\nSide >> "))
        area = Side ** 2
    elif choice == 4 or choice == "circle":
        radius = int(input("\nRadius >> "))
        area = math.pi * (radius ** 2)
    elif choice == 5 or choice == "quit":
        print("\nExiting...")
        break
    else:
        print("\nInvalid Input...")
        print("Restarting now")
        os.system("cls")
        continue
    
    
    print("Your area is", area)
    break