print("Enter Height  in cm: ")
cm = float(input())
print("Enter Weight in Kg: ")
weight_kg = float(input())
height_m = .01*cm


bmi = weight_kg/(height_m**2)

print("\n\n\n\nYour BMI is : "+str(round(bmi,2)))

perfect_weight = 25*(height_m**2)

if bmi<18.5:
    print("Underweight!")
elif 18.5<bmi<24.9:
    print("Wow ,Normal Weight!!!")
elif 25<bmi<29.9:
    print("You are overweight!!!")
    print ("Your maximum healthy weight based on a BMI of 25 is :"+str(round(perfect_weight,2))+" Kg")
    print ("You have to lose your weight min "+str(round(weight_kg-perfect_weight,2))+" Kg")
elif 30<bmi<34.9:
    print("You are overweight!!!\n Class (I) Obese")
    print ("Your maximum healthy weight based on a BMI of 25 is :"+str(round(perfect_weight,2))+" Kg")
    print ("You have to lose your weight min "+str(round(weight_kg-perfect_weight,2))+" Kg")
elif 35<bmi<39.9:
    print("You are overweight!!!\n Class (II) Obese")
    print ("Your maximum healthy weight based on a BMI of 25 is :"+str(round(perfect_weight,2))+" Kg")
    print ("You have to lose your weight min "+str(round(weight_kg-perfect_weight,2))+" Kg")
elif bmi>40:
    print("You are overweight!!!\n Class (III) Obese")
    print ("Your maximum healthy weight based on a BMI of 25 is :"+str(round(perfect_weight,2))+" Kg")
    print ("You have to lose your weight min "+str(round(weight_kg-perfect_weight,2))+" Kg")
else:
    print ("Serious condition. BMI 40++")
    print ("Your maximum healthy weight based on a BMI of 25 is :"+str(round(perfect_weight,2))+" Kg")
    print ("You have to lose your weight min "+str(round(weight_kg-perfect_weight,2))+" Kg")


k = input("please press enter to exit")
