#name_char = len(input("what is you name?"))
#new_name_char = str(name_char)
#print(type (new_name_char))
#print(new_name_char)


#BODMAS rule
a = float(100.5)
print(type(a))
print(70 + float(100.5))
print(str(70) + str(100))

#EX: 1 - type cast example: calculate sum of two digit number
print("--------------Exercise 1 to calculate sum of 2 digits------------------")
num = input("type a two digit number")
a= int(num[0])
b=int (num[1])
sum= a+b
new_sum= str(sum)
print("sum of two digit number is :" + new_sum)

#ex2:

print("--------------Exercise 2------------------")
print("The result of output1:"+str(3*3+3/3-3))
print("The result of output2:"+str(3*(3+((3/3)-3))))

#Ex3: BMI calculator (weight(kg)/(height**2)metersq)
print("--------------Exercise 3 to calculate BMI------------------")
weight=int(input("Please enter your weight in kg:"))
height=float(input("please enter your height in meters:"))
bmi=weight/height**2
#f-string: which combines different datatypes in one print statement
print(f"your weight is: {weight} kg, your height is: {height} sqmts, your bmi is :{bmi}")
#print(bmi)

#Ex4: 1 yr= 12 months, 1yr=365 days, 1 yr=52 weeks
print("--------------Exercise 4 to calculate time to live------------------")
age= input("Please enter your age:")
years_left=90-int(age)
#print(years_left)
months_left=years_left*12
#print(months_left)
weeks_left=years_left*52
#print(weeks_left)
days_left=years_left*365
print(f"Years left to live {years_left} years, months left to live {months_left} months,weeks left to live {weeks_left} weeks, days left to live {days_left} days")


#Ex5:tip calculator
print("--------------Exercise 5 to calculate tip------------------")
bill= input("what is your bill amount? ")
split = input("how many people would you like the bill to be split between? ")
tip_cont= input("how much percentage of bill would you like to tip? 10, 12 or 15 :")
#percentage = (float(bill)*int(tip_cont))/100
#total_bill=float(bill)+float(percentage)
ind_bill=(float(bill)+(float(bill)*int(tip_cont)/100))/int(split)
round_bill = "{:.2f}".format(ind_bill)
print(f"The amount to be paid by each one is {round_bill} pounds")

