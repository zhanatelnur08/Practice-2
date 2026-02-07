a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33  
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 200
b = 33 
c = 500
if not a > b:
  print("a is NOT greater than b")  

temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for Football")

  age=18
  weight=75
  length=180
  if(age > 18 and weight > 70) or length > 170:
    print("You can join the football team")