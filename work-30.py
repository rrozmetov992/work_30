#21-misol
#n = int(input("n = "))
#bor = False

#while n > 0:
#    if (n % 10) % 2 == 1:
#        bor = True
#    n //= 10

#print("Toq raqam bor:", bor)
#22-misol
#n = int(input("n = "))
#i = 2
#tub = True
#while i * i <= n:
#    if n % i == 0:
#        tub = False
#        break
#    i += 1
#print("Tub son:", tub)

#23-misol
#a = int(input("a = "))
#b = int(input("b = "))
#while a != b:
#    if a > b:
#        a = a - b
#    else:
#        b = b - a

#print("EKUB =", a)


#24-misol
#n = int(input("n = "))
#f1 = 1
#f2 = 1
#if n == 1:
#    print("Fibonacci soni: True")
#else:
#    while f2 < n:
#        f1, f2 = f2, f1 + f2
#    print("Fibonacci soni:", f2 == n)

#25-misol
#n = int(input("n = "))
#f1 = 1
#f2 = 1
#while f2 <= n:
 #   f1, f2 = f2, f1 + f2
#print("Birinchi katta Fibonacci =", f2)
#26-misol
#n = int(input("n = "))
#f1 = 1
#f2 = 1
#while f2 < n:
#    f1, f2 = f2, f1 + f2
#oldingi = f1
#keyingi = f1 + f2
#print("Oldingi Fibonacci =", oldingi)
#print("Keyingi Fibonacci =", keyingi)
#27-misol
#n = int(input("n = "))
#f1 = 1
#f2 = 1
#k = 2
#if n == 1:
#    print("Tartib raqami: 1 yoki 2")
#else:
#    while f2 < n:
#        f1, f2 = f2, f1 + f2
#        k += 1
#    if f2 == n:
#        print("Tartib raqami:", k)
#    else:
#        print("Bu Fibonacci soni emas")
#28-misol
#e = float(input("e = "))
#a_prev = 2
#k = 1
#while True:
 #   a = 2 + 1 / a_prev
 #   k += 1
 #   if abs(a - a_prev) < e:
 #       break
 #   a_prev = a
#print("Eng kichik k =", k)
#print("a_k =", a)
#print("a_(k-1) =", a_prev)
#29-misol
#e = float(input("e = "))
#a1 = 1
#a2 = 2
#k = 2
#while True:
#   a = (a1 + 2 * a2) / 3
#    k += 1
#    if abs(a - a2) < e:
#        break
#   a1, a2 = a2, a
#print("Eng kichik k =", k)
#print("a_k =", a)
#print("a_(k-1) =", a2)
#30-misol
#A = int(input("A = "))
#B = int(input("B = "))
#C = int(input("C = "))
#countA = 0
#tempA = A
#while tempA >= C:
#    tempA -= C
#    countA += 1
#countB = 0
#tempB = B
#while tempB >= C:
#    tempB -= C
#    countB += 1
#result = 0
#i = 0
#while i < countA:
#    result += countB
#    i += 1
#print("Kvadratlar soni =", result)
