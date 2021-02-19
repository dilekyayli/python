def yuvarla(s):
  return round(s+0.000001, 0)

def odevnotuhesapla(v):
  odevnotu = 50 + v/2
  return odevnotu
def orthesapla(v,o,f):
  ort = v*0.3 + o*0.2 + f*0.5
  return ort
vize = 60
final = 55

odev = odevnotuhesapla(vize)
print('odevnotu: ', odev)

ort = orthesapla(vize, odev, final)
print('ort: ', ort)

orty = round(ort, 0)
print('orty: ', orty)

ortyeni = yuvarla(ort)
print('ortyeni: ', ortyeni)

print("--------------------")

n = 11
for i in range(1,n):
  print(i, end='')
print()

s= 'Matematik'
for i in s:
  print(i, end='')
print()

for i in range(len(s)):
  print(i, '->', s[i])

print("--------------------")

s = '160a95!253.20'
b = False
for i in range(len(s)):
  if not (s[i] in '0123456789'):
    b = True
if b == True:
  print('girilen veride rakamlardan başka karakterler var.')
print("--------------------")

def buyukharfecevir(s):
  s = s.replace('ğ', 'Ğ')  # replace->yerine koy
  s = s.replace('ü', 'Ü')  # upper() ->büyük harfe çevir
  s = s.replace('ş', 'Ş')
  s = s.replace('i', 'İ')
  s = s.replace('ı', 'I')
  s = s.replace('ö', 'Ö')
  s = s.replace('ç', 'Ç')
  
  s = s.upper()
  return s
s = 'Bu gün hava çok Güzel. ğüşiıöç'
print('büyük harfe çevirmeden önce: ')
print(s)
print()
s = buyukharfecevir(s)
print('BÜYÜK HARFE çevirdikten sonra: ')
print(s)