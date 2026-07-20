import math as m
Wave_Amplituted1=10000
Wave_Amplituted2=1000000
Magnitute_Wave1= m.log10(Wave_Amplituted1)
Magnitute_Wave2=m.log(Wave_Amplituted2)
Difference=10**(Magnitute_Wave2-Magnitute_Wave1)
print()
print("Wave Amplituted 1: ",Wave_Amplituted1)
print("Wave Magnitute 1:",int(Magnitute_Wave1))
print("-------------------------------------")
print("Wave Amplituted 2: ",Wave_Amplituted2)
print("Wave Magnitute 2:",int(Magnitute_Wave2))
print("-------------------------------------")
print("The Difference is ",int(Difference),"Times Then ",Magnitute_Wave1)




