import math

print("--------------------")
print("100 hücre problemi")
print("--------------------")

n = 1001
d = {}
for i in range(1, n):
  d[i] = -1
for i in range(1, n):
  for j in range(i, n, i):
    d[j] = -d[j]
for i in range(1, n):
  if d[i] == +1:
    print(i, ".kapı açık...")

print("-------------------")
print("100-999 arasında rakamları küpleri toplamı kendisine eşit olan sayılar")
print("---------------------")

for i in range(1, 10):
  for j in range(0, 10):
    for k in range(0, 10):    #iç içe döngü 
      for p in range(0, 10):
        if i * 1000 + j * 100 + k * 10 + p == i ** 4 + j ** 4 + k ** 4 + p ** 4:
          print(i * 1000 + j * 100 + k * 10 + p )

print("--------------------")
print("1-1000 arasındaki asal sayılar")
print("-------------------")

print("%5d%5d" %(2,3), end=" ")
n = 1001       #Bir sayı kareköküne kadar olan sayılara bölünmüyorsa o sayı asal sayıdır.
i =5; k=2
while i < n:
  j =3; bolunuyor = False
  while j <= math.sqrt(i):
    if i/j == int(i/j):
      bolunuyor = True
      j+=2
    if bolunuyor == False:
      print("%5d" %i, end=" ")
      k += 1
      if k == 8:
        print()
        k=0
    i +=2

print("--------------------")
print("n.mertebeden pascal üçgeni")
print("--------------------")

n = 16
d = {}
for i in range(1, n+1):
  for j in range(1, i+1):
    if j == 1 or j == i:
      d[i,j] = 1          #iki boyutlu dizi
    else:
      d[i,j] = d[i-1,j] + d[i-1,j-1]
    print("%5d" %d[i,j], end=" ")
  print()