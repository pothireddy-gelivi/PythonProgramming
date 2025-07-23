#WAP to find maximum number among 5 numbers ?

num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
num3=int(input("Enter the number: "))
num4=int(input("Enter the number: "))
num5=int(input("Enter the number: "))
if num1>num2:
    if num1>num3:
        if num1>num4:
            if num1>num5:
                print(f"{num1} is maximum number.")
            else:
                print(f"{num5} is maximum number.")
        else:
            if num4>num5:
                print(f"{num4} is maximum number.")
            else:
                print(f"{num5} is maximum number.")
    else:
        if num3>num4:
            if num3 > num5:
                print(f"{num3} is maximum number.")
            else:
                print(f"{num5} is maximum number.")
        else:
            if num4>num5:
                print(f"{num4} is maximum number.")
            else:
                print(f"{num5} is maximum number.")
else:
    if num2>num3:
        if num2>num4:
            if num2>num5:
                print(f"{num2} is maximum number.")
            else:
                print(f"{num5} is maximum number.")
        else:
            if num4>num5:
                print(f"{num4} is maximum number.")
            else:
                print(f"{num5} is maximum number.")
    else:
        if num3>num4:
            if num3>num5:
                print(f"{num3} is maximum number.")
            else:
                print(f"{num5} is maximum number.")
        else:
            if num4>num5:
                print(f"{num4} is maximum number.")
            else:
                print(f"{num5} is maximum number.")