# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_square=float(height)**2
bmi = float(weight)/height_square
if bmi<18.5:
  print(f"Your BMI is {bmi}, you are underweight")
elif bmi<25 and bmi>18.5:
  print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi<30 and bmi>25:
  print(f"Your BMI is {bmi}, you are slihtly overweight")
elif bmi<35 and bmi>30:
  print(f"Your BMI is {bmi}, you are obese")
else:
  print(f"Your BMI is {bmi}, you are clinically obese")



