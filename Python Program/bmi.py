
print("1. CM,KG")
print("2. M,KG")

print("Choose 1 or 2: ")
choose = int(input())

def bmi_cm_kg():
    print("Enter Height in Cm: ")
    height_cm = (float(input())*0.01)
    print("Enter weight in Kg: ")
    weight_kg = float(input())
 
    bmi = weight_kg/(height_cm**2)
    perfect_weight = 25*(height_cm**2)
    
    if bmi<25:
        print("You are Underweight")
    elif bmi==25:
        print("perfect weight")
    elif bmi>25:
        print("you are overweight")
        print("Your Perfect weight is :"+str(perfect_weight))
        print("You should try to lose min: "+str(weight_kg-perfect_weight))
    

def bmi_m_kg():
    print("Enter Height in Miter: ")
    height_m = float(input())
    print("Enter weight in Kg: ")
    weight_kg = float(input())
 
    bmi = weight_kg/(height_m**2)
    perfect_weight = 25*(height_m**2)
    
    if bmi<25:
        print("You are Underweight")
    elif bmi==25:
        print("perfect weight")
    elif bmi>25:
        print("you are overweight")
        print("Your Perfect weight is :"+str(perfect_weight))
        print("You should try to lose min: "+str(weight_kg-perfect_weight))
    

if choose==1:
    bmi_cm_kg()
elif choose==2:
    bmi_m_kg()
else:
    Print("Invalid Input")
    
k = input("Press enter to exit: ")

