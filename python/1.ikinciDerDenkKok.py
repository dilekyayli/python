import math
a = float(input("a katsayısını giriniz: "))
b = float(input("b katsayısını giriniz: "))
c = float(input("c katsayısını giriniz: "))
d = b*b - 4*a*c
if d < 0:
  print("gerçel kök yoktur.") 
if d == 0:
  print("çakışık kök vardır.")
  x = -b/(2*a)
  print("x: ",x)
if d > 0:
  print("gerçel iki kök vardır.")
  x1 =(-b - (math.sqrt(d)))/(2*a)
  x2 =(-b + math.sqrt(d))/(2*a)
  print("x1: ",x1)
  print("x2: ",x2)