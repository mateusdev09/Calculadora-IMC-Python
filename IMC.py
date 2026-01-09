Massa = float(input("digite sua massa corporal: " ))
Altura = float(input("digite sua altura: "))

IMC = Massa / (Altura * Altura)
print (f"IMC: , {IMC:.2f}")

if (IMC < 17) :
    print ("voce esta muito abaixo do peso ")
    print ("consulte um medico especializado ")
elif (IMC >= 17) and (IMC < 18.5) :
    print ("voce esta abaixo do peso ")
elif (IMC >= 18.5) and (IMC < 25) :
    print ("voce esta no peso ideal ")
elif (IMC >= 25) and (IMC < 30) :
    print ("voce esta com sobrepeso ")
elif (IMC >= 30) and (IMC < 35) :
    print ("voce esta com obesidade ")
elif (IMC >= 35) and (IMC < 40) :
    print ("voce esta com obesidade severa ")
    print ("consulte um medico especializado ")
else :
    print ("voce esta com obesidade morbida ")
    print ("procure um medico com urgencia! ")
