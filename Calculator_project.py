#Aurthor : Nathishwar
import math as m

# Simple Calculator Program 
class calculator:
    def main_fun():
        while True:
            try:
                print("*" *31 + "Main Menu" + "*" *31 + "\n"  )
                print(" \t (A)-Addition \t \t (S)-Subtraction \n \t (M)-Multiply \t \t (D)-Division \n \t (P)-Power \t \t (SQ)-Square Root \n \t (C)-cos\t \t (SN)-sin \n \t (T)-Tan \t\t (F)-factorial \n\n \t\t    (E)-Exit ")

                n = input("Enter the operation to perform :").upper()

            except Exception:
                print("You entered the invalid Data type:")

            else:
                if n =='A':
                    print("*" *31 + "Addition" + "*" *31 + "\n" * 1 )
                    calculator.addtion()
                elif n=="S":
                    print("*" *31 + "Subtraction" + "*" *31 + "\n" * 1 )
                    calculator.subtraction()
                elif n=="M":
                    print("*" *31 + "Multiply" + "*" *31 + "\n" * 1 )
                    calculator.multiplication()
                elif n=="D":
                    print("*" *31 + "Division" + "*" *31 + "\n" * 1 )
                    calculator.division()
                elif n=="P":
                    print("*" *31 + "Power" + "*" *31+  "\n" * 1 )
                    calculator.power()

                elif n=="SQ":
                    print("*" *31 + "Square Root" + "*" *31+  "\n" * 1 )
                    try:
                        x= int(input("Enter the number : "))
                    except ValueError:
                        print("Entered the invalid Data type !")
                    else:
                        k = m.sqrt(x)
                        print(f"Square Root of {x} is {round(k)}")
                    finally:
                        print("\n")

                elif n=="C":
                    print("*" *31 + "Cosine" + "*" *31+  "\n" * 1 )
                    try:
                        x= float(input("Enter the number : "))
                    except ValueError:
                        print("Entered the invalid Data type !")
                    else:
                        k = m.cos(x)
                        print(f"Cos of {x} in radians is : {k}")
                    finally:
                        print("\n")

                elif n=="SN":
                    print("*" *31 + "Sine" + "*" *31+  "\n" * 1 )
                    try:
                        x= float(input("Enter the number : "))
                    except ValueError:
                        print("Entered the invalid Data type !")
                    else:
                        k = m.sin(x)
                        print(f"sin of {x}in radians is : {k}")
                    finally:
                        print("\n")

                elif n=="T":
                    print("*" *31 + "Tangent" + "*" *31+  "\n" * 1 )
                    try:
                        x= float(input("Enter the number : "))
                    except ValueError:
                        print("Entered the invalid Data type !")
                    else:
                        k = m.tan(x)
                        print(f"Tangent of {x}in radians is : {k}")
                    finally:
                        print("\n")

                elif n=="F":
                    print("*" *31 + "Factorial" + "*" *31+  "\n" * 1 )
                    try:
                        x= int(input("Enter the number : "))
                    except ValueError:
                        print("Entered the invalid Data type !")
                    else:
                        k = m.factorial(x)
                        print(f"Factorial of {x} is {k}")
                    finally:
                        print("\n")

                elif n=="E":
                    print("*" *31 + "Thankyou" + "*" *31 + "\n" * 1)
                    break
                
                else:
                    print("Please Enter the valid input !")

            finally:
                print("\n")

    def addtion():
        while True:
            try:
                x= int(input("How many numbers need to Add! : "))

            except ValueError:
                print("You entered the incorrect data format\n")

            else:
                if x==0 or x==1:
                    print("Please enter more than one element")
                    continue
                else :
                    list1 =[]
                    for i in range(x): # result = sum(list1)
                        y = float(input("Enter the number:"))
                        list1.append(y)

                    result =0
                    for k in list1:
                        result+=k

                    print(f"The value is :{result}")

            finally:
                

                ele = input("Do you want to Continue Addition(Y/N)! :").upper()
                if ele == "Y":
                    continue
                else:
                    break



    def subtraction():
        while True:
            try:
                x,y=float(input("Enter the first no : ")), float(input("Enter the second no :"))

            except ValueError :
                print("You entered the incorrect data format\n")

            else:
                z= x-y
                print(f"The value of {x}-{y} = {z}")
            finally:   
                ele = input("Do you want to continue Subraction operation (Y/N):").upper()

                if ele == "Y":
                    continue
                else:
                    break

    def multiplication():
        while True:
            try:
                x,y=float(input("Enter the first no : ")), float(input("Enter the second no :"))

            except ValueError :
                print("You entered the incorrect data format\n")
            else:
                z= x*y
                print(f"The value of {x} X {y} = {z}")

            finally:
                ele = input("Do you wantto continue multiplication operation (Y/N):").upper()

                if ele == "Y":
                    continue
                else:
                    break

    def division():
        while True:
            try:
                x,y=float(input("Enter the first no : ")), float(input("Enter the second no :"))

            except ValueError :
                print("You entered the incorrect data format\n")
            else:
                z= x/y
                print(f"The value of {x}/{y} = {z}")

            finally:
                ele = input("Do you want to continue division operation (Y/N):").upper()

                if ele == "Y":
                    continue
                else:
                    break

    def power():
        while True:
            try:
                x,y=int(input("Enter the base no : ")), int(input("Enter the power no :"))
            except ValueError :
                print("You entered the incorrect data format\n")
            else:
                z= x**y
                print(f"The value of {x}^{y} = {z}")
            finally:
                ele = input("Do you want to continue power operation (Y/N):").upper()

                if ele == "Y":
                    continue
                else:
                    break

    

calculator.main_fun()
