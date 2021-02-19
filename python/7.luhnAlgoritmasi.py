def luhn_kontrol(s):
  n = 16
  d1 = {}
  d2 = {}
  for i in range(1, n+1):
    d2[i] = int(s[i-1])
  for i in range(1, n+1):
    if i % 2 !=0:
      d1[i] = 2 * d2[i]
      if d1[i] > 9:
        d1[i] = int(d1[i]/10) + d1[i] % 10
    else:
      d1[i] = d2[i]
  tekler_toplami = 0
  ciftler_toplami = 0
  for i in range(1, n+1):
    if i % 2 !=0:
      tekler_toplami += d1[i]
    else:
      ciftler_toplami += d1[i]
  toplam = tekler_toplami + ciftler_toplami
  kalan = toplam % 10
  if kalan == 0:
    return True
  else:
    return False

def son_digit_dogrulama(s):
  n = 16
  d1 = {}
  d2 = {}
  for i in range(1, n+1):
    d2[i] = int(s[i-1])
  for i in range(1, n):
    d1[i] = d2[n-i]
  for i in range(1, n):
    if i % 2 !=0:
      d1[i] = 2 * d1[i]
      if d1[i] > 9: d1[i] -=9
  toplam = 0
  for i in range(1, n):
    toplam += d1[i]
  kalan = 9 * toplam % 10
  if kalan == d2[n]:
    return True, kalan
  else:
    return False, -1

s1 = "5492968795874876"
print("------------1.tip doğrulama------------")
if luhn_kontrol(s1) == True:
  print(s1 + "-BU KART NO GEÇERLİDİR.")
else:
  print(s1 + "-BU KART NO GEÇERLİ DEĞİLDİR.")

print("--------------2.tip doğrulama sondigit--------------")

sonuc, sondigit = son_digit_dogrulama(s1)
if sonuc == True:
  print(s1 + "-BU KART NO GEÇERLİDİR. sondigit: ", sondigit)
else:
  print(s1 + "-BU KART NO GEÇERLİ DEĞİLDİR.")