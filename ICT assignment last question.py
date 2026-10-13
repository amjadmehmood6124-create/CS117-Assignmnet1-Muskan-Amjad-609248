def star_to_delta(Ra, Rb, Rc):
 RNumerator = (Ra*Rb)+(Rb*Rc)+(Rc*Ra)
 Rab=RNumerator/Rc
 Rbc=RNumerator/Ra
 Rca=RNumerator/Rb
 Rab=round (Rab, 2)
 Rbc=round (Rbc, 2)
 Rca=round (Rca, 2)
 return(Rab,Rbc,Rca)
R1=int(input("Enter the value of resistance R1: "))
R2=int(input("Enter the value of resistance R2: "))
R3=int(input("Enter the value of resistance R3: "))
print(star_to_delta(R1, R2, R3))

    
